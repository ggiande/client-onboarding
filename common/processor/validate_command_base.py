from common.processor.command_abc import CommandABC
from abc import abstractmethod
from sqlalchemy.orm import Session

class ValidateCommandBase(CommandABC):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def post_process(self) -> None:
        pass

    def handle_exception(self) -> None:
        pass

    def handle_command_execution_exception(self) -> None:
        pass

    def is_telemetry_turned_on(self) -> bool:
        return False

    def get_event_region_name(self) -> str:
        return ""

    def is_command_applicable(self, data: dict) -> bool:
        return data.get("is_applicable")

    @abstractmethod
    def execute(self, data: dict, db_session: Session) -> None:
        pass
