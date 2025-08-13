from common.processor import SaveCommandBase
from sqlalchemy.orm import Session

class RequestSaveCommand(SaveCommandBase):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def save(self) -> bool:
        return False

    def is_command_applicable(self, data: dict) -> bool:
        return False

    def execute(self, data: dict, db_session: Session) -> dict:
        if not self.is_command_applicable(data):
            return data
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")
        print("Sending the request...")
        # Simulate an external call
        data['sent'] = True
        return data
