import uuid
from abc import ABCMeta, abstractmethod

from flowcept.commons.flowcept_dataclasses.workflow_object import (
    WorkflowObject,
)
from flowcept.flowcept_api.db_api import DBAPI
from flowcept.commons.utils import get_utc_now, fill_with_basic_workflow_info
from flowcept.configs import (
    FLOWCEPT_USER,
    SYS_NAME,
    NODE_NAME,
    LOGIN_NAME,
    PUBLIC_IP,
    PRIVATE_IP,
    CAMPAIGN_ID,
    HOSTNAME,
    EXTRA_METADATA,
    ENRICH_MESSAGES,
)
from flowcept.commons.flowcept_logger import FlowceptLogger
from flowcept.commons.daos.mq_dao import MQDao
from flowcept.commons.flowcept_dataclasses.task_object import TaskObject
from flowcept.commons.settings_factory import get_settings

from flowcept.flowceptor.telemetry_capture import TelemetryCapture

from flowcept.version import __version__


# TODO :base-interceptor-refactor: :ml-refactor: :code-reorg: :usability:
#  Consider creating a new concept for instrumentation-based 'interception'.
#  These adaptors were made for data observability.
#  Perhaps we should have a BaseAdaptor that would work for both and
#  observability and instrumentation adapters. This would be a major refactor
#  in the code. https://github.com/ORNL/flowcept/issues/109
# class BaseInterceptor(object, metaclass=ABCMeta):
class BaseInterceptor(object):
    def __init__(self, plugin_key):
        self.logger = FlowceptLogger()
        if (
            plugin_key is not None
        ):  # TODO :base-interceptor-refactor: :code-reorg: :usability:
            self.settings = get_settings(plugin_key)
        else:
            self.settings = None
        self._mq_dao = MQDao()
        self._db_api = DBAPI()
        self._bundle_exec_id = None
        self._interceptor_instance_id = str(id(self))
        self.telemetry_capture = TelemetryCapture()
        self._generated_workflow_id = False
        self._registered_workflow = False

    def _enrich_task_message(self, settings_key, task_msg: TaskObject):
        if task_msg.utc_timestamp is None:
            task_msg.utc_timestamp = get_utc_now()

        if task_msg.adapter_id is None:
            task_msg.adapter_id = settings_key

        if task_msg.user is None:
            task_msg.user = FLOWCEPT_USER

        if task_msg.campaign_id is None:
            task_msg.campaign_id = CAMPAIGN_ID

        if task_msg.sys_name is None:
            task_msg.sys_name = SYS_NAME

        if task_msg.node_name is None:
            task_msg.node_name = NODE_NAME

        if task_msg.login_name is None:
            task_msg.login_name = LOGIN_NAME

        if task_msg.public_ip is None and PUBLIC_IP is not None:
            task_msg.public_ip = PUBLIC_IP

        if task_msg.private_ip is None and PRIVATE_IP is not None:
            task_msg.private_ip = PRIVATE_IP

        if task_msg.hostname is None and HOSTNAME is not None:
            task_msg.hostname = HOSTNAME

        if task_msg.extra_metadata is None and EXTRA_METADATA is not None:
            task_msg.extra_metadata = EXTRA_METADATA

        if task_msg.flowcept_version is None:
            task_msg.flowcept_version = __version__

        if task_msg.workflow_id is None and not self._generated_workflow_id:
            task_msg.workflow_id = str(uuid.uuid4())
            self._generated_workflow_id = True

    def prepare_task_msg(self, *args, **kwargs) -> TaskObject:
        raise NotImplementedError()

    def start(self, bundle_exec_id) -> "BaseInterceptor":
        """
        Starts an interceptor
        :return:
        """
        self._bundle_exec_id = bundle_exec_id
        self._mq_dao.start_time_based_flushing(
            self._interceptor_instance_id, bundle_exec_id
        )
        self.telemetry_capture.init_gpu_telemetry()
        return self

    def stop(self) -> bool:
        """
        Gracefully stops an interceptor
        :return:
        """
        self._mq_dao.stop_time_based_flushing(
            self._interceptor_instance_id, self._bundle_exec_id
        )
        self.telemetry_capture.shutdown_gpu_telemetry()

    def observe(self, *args, **kwargs):
        """
        This method implements data observability over a data channel
         (e.g., a file, a DBMS, an MQ)
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def callback(self, *args, **kwargs):
        """
        Method that implements the logic that decides what do to when a change
         (e.g., task state change) is identified.
        If it's an interesting change, it calls self.intercept; otherwise,
        let it go....
        """
        raise NotImplementedError()

    def register_workflow(self, task_msg: TaskObject):
        self._registered_workflow = True
        if task_msg.workflow_id is None:
            return

        workflow_obj = WorkflowObject()
        workflow_obj.workflow_id = task_msg.workflow_id
        fill_with_basic_workflow_info(workflow_obj)
        workflow_obj.interceptor_ids = [self._interceptor_instance_id]

        machine_info = self.telemetry_capture.capture_machine_info()
        if machine_info is not None:
            if workflow_obj.machine_info is None:
                workflow_obj.machine_info = {}
            # TODO :refactor-base-interceptor: we might want to register machine info even when there's no observer
            workflow_obj.machine_info[
                self._interceptor_instance_id
            ] = machine_info

        self._db_api.insert_or_update_workflow(workflow_obj)

    def intercept(self, task_msg: TaskObject):
        if (
            self._mq_dao._buffer is None
        ):  # TODO :base-interceptor-refactor: :code-reorg: :usability:
            raise Exception(
                f"This interceptor {id(self)} has never been started!"
            )

        if ENRICH_MESSAGES:
            if (
                self.settings is not None
            ):  # TODO :base-interceptor-refactor: :code-reorg: :usability: revisit all times we assume settings is not none
                key = self.settings.key
            else:
                key = None
            self._enrich_task_message(key, task_msg)

        if not self._registered_workflow:
            self.register_workflow(task_msg)

        _msg = task_msg.to_dict()
        self.logger.debug(
            f"Going to send to Redis an intercepted message:"
            f"\n\t[BEGIN_MSG]{_msg}\n[END_MSG]\t"
        )
        self._mq_dao.publish(_msg)
