from perun.connector.utils.Logger import Logger
from perun.connector.models.MemberStatusEnum import MemberStatusEnum
from perun.connector.adapters.AdaptersManager import AdaptersManager
from perun.connector.adapters.AdaptersManager import (
    AdaptersManagerNotExistsException,
)
from perun.connector.adapters.AdaptersManager import AdaptersManagerException
from satosa.micro_services.base import ResponseMicroService
from satosa.exception import SATOSAError
from satosa.response import Redirect
from satosacontrib.perun.utils.ConfigStore import ConfigStore
from satosacontrib.perun.utils.Utils import Utils


class EnsureMember(ResponseMicroService):
    """
    This Satosa microservice checks member status
    of the user and calls registration if needed
    """

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.LOG_PREFIX = "perun:EnsureMember: "
        self.REGISTER_URL = "register_url"
        self.VO_SHORT_NAME = "vo_short_name"
        self.GROUP_NAME = "group_name"
        self.CALLBACK_PARAMETER_NAME = "callback_parameter_name"
        self.PARAM_REGISTRATION_URL = "registration_url"

        self.__logger = Logger.get_logger(self.__class__.__name__)

        self.__config = config
        self.__global_cfg = ConfigStore.get_global_cfg(config["global_cfg_path"])
        self.__attr_map_cfg = ConfigStore.get_attributes_map(
            self.__global_cfg["attrs_cfg_path"]
        )
        self.__allowed_requesters = self.__global_cfg.get("allowed_requesters", {})
        self.__adapters_manager = AdaptersManager(
            self.__global_cfg["adapters_manager"], self.__attr_map_cfg
        )

        self.__signing_cfg = self.__global_cfg["jwk"]

        if (
            self.REGISTER_URL not in self.__config
            or not self.__config[self.REGISTER_URL]
        ):
            raise SATOSAError(
                self.LOG_PREFIX
                + "Missing configuration option '"
                + self.REGISTER_URL
                + "'"
            )
        self.__register_url = self.__config[self.REGISTER_URL]

        if (
            self.CALLBACK_PARAMETER_NAME not in self.__config
            or not self.__config[self.CALLBACK_PARAMETER_NAME]
        ):
            raise SATOSAError(
                self.LOG_PREFIX
                + "Missing configuration option '"
                + self.CALLBACK_PARAMETER_NAME
                + "'"
            )
        self.__callback_param_name = self.__config[self.CALLBACK_PARAMETER_NAME]

        if (
            self.VO_SHORT_NAME not in self.__config
            or not self.__config[self.VO_SHORT_NAME]
        ):
            raise SATOSAError(
                self.LOG_PREFIX
                + "Missing configuration option '"
                + self.VO_SHORT_NAME
                + "'"
            )
        self.__vo_short_name = self.__config[self.VO_SHORT_NAME]

        self.__group_name = self.__config[self.GROUP_NAME]

        self.__unauthorized_redirect_url = self.__config["unauthorized_redirect_url"]

        self.__registration_result_url = self.__config["registration_result_url"]  # noqa

        self.__endpoint = "/process"

    def process(self, context, data):
        """
        This is where the micro service should modify the request / response.
        Subclasses must call this method (or in another way make sure the
        next callable is called).
        @param context: The current context
        @param data: Data to be modified
        """

        if not Utils.allow_by_requester(context, data, self.__allowed_requesters):
            return super().process(context, data)
        user_id = data.attributes.get(self.__global_cfg["perun_user_id_attribute"])  # noqa
        if not user_id:
            raise SATOSAError(
                self.LOG_PREFIX + f"Missing mandatory attribute "
                f"'{self.__global_cfg['perun_user_id_attribute']}' "  # noqa
                f"in data.attributes. Hint: Did you "
                f"configured PerunUser microservice "
                f"before this microservice?"
            )

        try:
            vo = self.__adapters_manager.get_vo(short_name=self.__vo_short_name)  # noqa
        except (
            AdaptersManagerException,
            AdaptersManagerNotExistsException,
        ) as e:
            self.__logger.debug(e)
            vo = None

        if not vo:
            raise SATOSAError(
                self.LOG_PREFIX
                + "VO with vo_short_name '"
                + self.__vo_short_name
                + "' not found."
            )

        self.__handle_user(user_id, vo, data, context)

        return super().process(context, data)

    def __handle_user(self, user, vo, data, context):
        """
        Handles user according to his member status
        @param user: current user
        @param vo: current vo
        @param data: microservice data
        @param context: microservice context
        @return: None
        """
        is_user_in_group = not self.__group_name or self.__is_user_in_group(user, vo)
        member_status = self.__adapters_manager.get_member_status_by_user_and_vo(
            user, vo
        )

        if member_status == MemberStatusEnum.VALID and is_user_in_group:
            self.__logger.debug(self.LOG_PREFIX + "User is allowed to continue.")

            return

        member_status = self.__adapters_manager.get_member_status_by_user_and_vo(
            user, vo
        )  # noqa
        vo_has_registration_form = self.__adapters_manager.has_registration_form_vo(vo)
        group_has_registration_form = self.__group_has_registration_form(vo)

        if member_status == MemberStatusEnum.VALID and is_user_in_group:
            self.__logger.debug(self.LOG_PREFIX + "User is allowed to continue.")
        elif (
            member_status == MemberStatusEnum.VALID
            and not is_user_in_group
            and group_has_registration_form
        ):
            self.__logger.debug(
                self.LOG_PREFIX
                + "User is not valid in group "
                + self.__group_name
                + " - sending to registration."
            )
            self.register(context, data, self.__group_name)
        elif not member_status and vo_has_registration_form and is_user_in_group:
            self.__logger.debug(
                self.LOG_PREFIX
                + "User is not member of vo "
                + self.__vo_short_name
                + " - sending to registration."
            )
            self.register(context, data)
        elif (
            not member_status
            and vo_has_registration_form
            and not is_user_in_group
            and group_has_registration_form
        ):
            self.__logger.debug(
                self.LOG_PREFIX
                + "User is not member of vo "
                + self.__vo_short_name
                + " and is not in group "
                + self.__group_name
                + " - sending to registration."
            )
            self.register(context, data, self.__group_name)
        elif (
            member_status == MemberStatusEnum.EXPIRED
            and vo_has_registration_form
            and is_user_in_group
        ):
            self.__logger.debug(
                self.LOG_PREFIX + "User is expired - sending to registration."
            )
            self.register(context, data)
        elif (
            member_status == MemberStatusEnum.EXPIRED
            and not is_user_in_group
            and vo_has_registration_form
            and group_has_registration_form
        ):
            self.__logger.debug(
                self.LOG_PREFIX
                + "User is expired and not in group "
                + self.__group_name
                + " - sending to registration."
            )
            self.register(context, data, self.__group_name)
        else:
            self.__logger.debug(
                self.LOG_PREFIX + "User is not valid in vo/group and cannot"
                " be sent to the registration - sending to unauthorized"
            )
            self.unauthorized(context, data)

    def __is_user_in_group(self, user, vo):
        try:
            member_groups = (
                self.__adapters_manager.get_groups_where_user_as_member_is_active(
                    user, vo
                )
            )  # noqa
        except (
            AdaptersManagerException,
            AdaptersManagerNotExistsException,
        ) as e:
            self.__logger.debug(e)
            member_groups = None

        for group in member_groups:
            if self.__group_name == group.name:
                return True

        return False

    def __group_has_registration_form(self, vo):
        try:
            group = self.__adapters_manager.get_group_by_name(vo, self.__group_name)
        except (
            AdaptersManagerException,
            AdaptersManagerNotExistsException,
        ) as e:
            self.__logger.debug(e)
            group = None

        if group is not None:
            return self.__adapters_manager.has_registration_form_group(group)

        return False

    def register(self, context, data, group_name=None):
        """
        Registers member according to given data
        @param context: current microservice context
        @param data: microservice data
        @param group_name: name of the group to register to
        @return: Redirect to registration url if possible
        """
        callback = ""  # ??
        if self.__callback_param_name:
            registration_url = self.__register_url + "?vo=" + self.__vo_short_name

            if group_name:
                registration_url += "&group=" + group_name

            self.__logger.debug(
                self.LOG_PREFIX
                + "Redirecting to '"
                + registration_url
                + ", callback parameter '"
                + self.__callback_param_name
                + "' set to value '"
                + callback
                + "'."
            )

            request_data = {  # noqa
                "targetnew": callback,
                "targetexisting": callback,
                "targetextended": callback,
            }

            return Utils.secure_redirect_with_nonce(
                context,
                data,
                request_data,
                registration_url,
                self.__signing_cfg,
                self.name,
            )

        else:
            raise SATOSAError(
                self.LOG_PREFIX
                + "No configuration for registration set. Cannot proceed."
            )

    def unauthorized(self, context, data):
        """
        Saves user state and redirects them away to a configurable url whenever
        they're not authorized for an operation within this microservice.
        @return: Redirect to a pre-configured url with "unauthorized" page
        """
        return Redirect(self.__unauthorized_redirect_url)

    def __handle_registration_response(self, context):
        context, data = Utils.handle_registration_response(
            context,
            self.__signing_cfg,
            self.__registration_result_url,
            self.name,
        )
        return self.process(context, data)

    def register_endpoints(self):
        """
        Registers an endpoint for external service reply when registering user
        into a group.
        @return: url of endpoint for external service to reply to and a method
                 to handle the reply
        """
        return [
            (
                f"^perunensuremember{self.__endpoint}$",
                self.__handle_registration_response,
            )
        ]
