from unittest.mock import patch, MagicMock

from perun.connector.adapters.AdaptersManager import AdaptersManager
from satosa.context import Context
from satosa.internal import InternalData
import satosacontrib.perun.micro_services.idm

from satosacontrib.perun.utils.ConfigStore import ConfigStore


class TestContext(Context):
    __test__ = False

    def __init__(self):
        super().__init__()
        self.internal_data["target_entity_id"] = "example_entity_id"


class TestData(InternalData):
    __test__ = False

    def __init__(self, data, attributes):
        super().__init__()
        self.data = data
        self.attributes = attributes
        self.auth_info = None
        self.requester = "example_requester"


class Loader:
    GLOBAL_CONFIG = {
        "eduperson_entitlement": "edu_person_entitlement",
        "forwarded_eduperson_entitlement": "forwarded_edu_person_entitlement",
        "perun_user_id_attribute": "example_user_id",
        "perun_login_attribute": "example_login",
        "attrs_cfg_path": "example_path",
        "adapters_manager": "adapters manager cfg info",
        "jwk": {
            "keystore": "example_keystore",
            "keyid": "example_keyid",
            "token_alg": "example_token_alg",
        },
        "allowed_requesters": {
            "": {"deny": ["forbidden_requester"]},
            "target_entity_id1": {"allow": ["allowed_requester"]},
            "target_entity_id2": {"deny": ["forbidden_requester"]},
        },
    }

    def __init__(self, config, name_of_microservice):
        self.config = config
        self.name = name_of_microservice

    @patch("satosacontrib.perun.utils.ConfigStore.ConfigStore.get_global_cfg")
    @patch("satosacontrib.perun.utils.ConfigStore.ConfigStore.get_attributes_map")  # noqa
    @patch("perun.connector.adapters.AdaptersManager.AdaptersManager.__init__")
    def create_mocked_instance(
        self, mock_request, mock_request2, mock_request3, perun_micro_service=False
    ):
        ConfigStore.get_global_cfg = MagicMock(return_value=Loader.GLOBAL_CONFIG)  # noqa
        ConfigStore.get_attributes_map = MagicMock(return_value=None)
        AdaptersManager.__init__ = MagicMock(return_value=None)
        my_class = (
            getattr(satosacontrib.perun.micro_services.idm, self.name)
            if perun_micro_service
            else getattr(satosacontrib.perun.micro_services, self.name)
        )
        return my_class(self.config, self.name, self.name + "Url")
