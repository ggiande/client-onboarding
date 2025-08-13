from abc import abstractmethod

from common.processor import CommandABC


class InitializeCommandBase(CommandABC):
    """Initializes default RequestContext

    Args:
        CommandABC (_type_): _description_
    """
    def is_telemetry_turned_on(self) -> bool:
        return False

    @abstractmethod
    def execute(self, data: dict) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def get_event_region_name(self) -> str:
        return ""

    def post_process(self) -> None:
        pass

    @abstractmethod
    def is_command_applicable(self) -> bool:
        pass