import copy
import logging
from unittest.mock import patch, MagicMock

import pytest
from perun.connector import User
from perun.connector.adapters.AdaptersManager import (
    AdaptersManager,
    AdaptersManagerNotExistsException,
)
from satosa.exception import SATOSAError
from satosa.internal import InternalData
from satosa.micro_services.base import MicroService

from satosacontrib.perun.micro_services.idm.perun_user import (
    PerunUser,
)  # noqa
from satosacontrib.perun.utils.Utils import Utils
from tests.test_microservice_loader import Loader
from tests.test_microservice_loader import TestContext

MICROSERVICE_CONFIG = {
    "global_cfg_path": "example_path",
    "internal_login_attribute": "example_internal_login",
    "internal_extsource_attribute": "example_internal_extsource",
    "proxy_extsource_name": "example_extsource_name",
    "registration_page_url": "example_url",
    "registration_result_url": "example_url",
}

MICROSERVICE = Loader(MICROSERVICE_CONFIG, "PerunUser").create_mocked_instance(
    perun_micro_service=True
)


@patch("satosa.context.Context.get_decoration")
def test_process_requester_not_allowed(mock_method, caplog):
    mock_method.return_value = "target_entity_id2"
    data_with_disallowed_requester = InternalData()
    data_with_disallowed_requester.requester = "forbidden_requester"
    disallowed_requester_log = "Requester 'forbidden_requester' is not allowed for 'target_entity_id2' due to deny rules"
    MicroService.process = MagicMock(return_value=None)
    with caplog.at_level(logging.DEBUG):
        MICROSERVICE.process(TestContext(), data_with_disallowed_requester)
        assert disallowed_requester_log in caplog.text
        MicroService.process.assert_called()


@patch("perun.connector.adapters.AdaptersManager.AdaptersManager.get_perun_user")
@patch(
    "satosacontrib.perun.micro_services.idm.perun_user.PerunUser.handle_user_not_found"  # noqa
)
def test_process_user_not_found(mock_request_1, mock_request_2):
    data_with_non_existent_user = InternalData()
    data_with_non_existent_user.requester = "allowed_req_1"
    data_with_non_existent_user.auth_info.issuer = "example_non_existent_name"
    data_with_non_existent_user.attributes["example_internal_login"] = []

    AdaptersManager.get_perun_user = MagicMock(
        side_effect=AdaptersManagerNotExistsException(
            '"name":"UserExtSourceNotExistsException"'
        )
    )
    PerunUser.handle_user_not_found = MagicMock(return_value=None)
    MICROSERVICE.process(TestContext(), data_with_non_existent_user)
    PerunUser.handle_user_not_found.assert_called()


@patch("perun.connector.adapters.AdaptersManager.AdaptersManager.get_perun_user")
@patch(
    "perun.connector.adapters.AdaptersManager.AdaptersManager.get_user_attributes"  # noqa
)
@patch("satosa.micro_services.base.MicroService.process")
def test_process_user_found(mock_request_1, mock_request_2, mock_request_3):
    data_with_existing_user = InternalData()
    data_with_existing_user.requester = "allowed_req_1"
    data_with_existing_user.auth_info.issuer = "example_existing_name"
    data_with_existing_user.attributes["example_internal_login"] = []
    example_user = User(1, "John Doe")

    AdaptersManager.get_perun_user = MagicMock(return_value=example_user)
    AdaptersManager.get_user_attributes = MagicMock(
        return_value={"perun_login_attribute": "example_login"}
    )
    MicroService.process = MagicMock(return_value=None)

    MICROSERVICE.process(TestContext(), data_with_existing_user)

    MicroService.process.assert_called()


def test_handle_user_not_found_missing_registration_link():
    config_without_registration_link = copy.deepcopy(MICROSERVICE_CONFIG)
    config_without_registration_link.pop("registration_page_url")
    microservice = Loader(
        config_without_registration_link, "PerunUser"
    ).create_mocked_instance(perun_micro_service=True)

    user_name = "example_name"
    user_logins = ["example_login_1", "example_login_2"]
    missing_registration_link_error_message = (
        f"User with name {user_name} and idp IDs {user_logins} was not found"
        " in Perun. And redirect link to registration page is missing in the"
        " config file."
    )

    with pytest.raises(SATOSAError) as error:
        microservice.handle_user_not_found(
            user_name, user_logins, TestContext(), InternalData()
        )

        assert str(error.value.args[0]) == missing_registration_link_error_message


@patch("satosacontrib.perun.utils.Utils.Utils.secure_redirect_with_nonce")
def test_handle_user_not_found_successful_redirect(mock_request_1):
    Utils.secure_redirect_with_nonce = MagicMock(return_value=None)
    MICROSERVICE.handle_user_not_found(None, None, None, None)

    Utils.secure_redirect_with_nonce.assert_called()


@patch("satosacontrib.perun.utils.Utils.Utils.handle_registration_response")
@patch("satosacontrib.perun.micro_services.idm.perun_user.PerunUser.process")  # noqa
def test_handle_registration_response(mock_request_1, mock_request_2):
    expected_result = "process result"
    Utils.handle_registration_response = MagicMock(
        return_value=(TestContext(), InternalData())
    )
    PerunUser.process = MagicMock(return_value=expected_result)

    result = MICROSERVICE._PerunUser__handle_registration_response(None)

    Utils.handle_registration_response.assert_called()
    PerunUser.process.assert_called()
    assert result == expected_result
