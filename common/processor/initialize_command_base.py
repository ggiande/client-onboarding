from abc import abstractmethod

from common.processor import CommandABC
from sqlalchemy.orm import Session

class InitializeCommandBase(CommandABC):
    """Initializes default RequestContext

    Args:
        CommandABC (_type_): _description_
    """
    def is_telemetry_turned_on(self) -> bool:
        return False

    @abstractmethod
    def execute(self, data: dict, db_session: Session) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def get_event_region_name(self) -> str:
        return ""

    def post_process(self) -> None:
        pass

    def is_command_applicable(self, data: dict) -> bool:
        return data.get("is_applicable")