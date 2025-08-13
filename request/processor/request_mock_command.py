from common.processor import MockCommandBase
from sqlalchemy.orm import Session
from overrides import override

class RequestMockCommand(MockCommandBase):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def execute(self, data: dict, db_session: Session) -> dict:
        if not self.is_command_applicable(data):
            return data
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")
        print("Mocking a command...")
        data['mocked'] = True
        return data
