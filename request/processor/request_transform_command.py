from common.processor import TransformCommandBase

from sqlalchemy.orm import Session
class RequestTransformCommand(TransformCommandBase):

    def is_command_applicable(self, data: dict) -> bool:
        pass

    def __init__(self, service_name: str):
        self.service_name = service_name

    def execute(self, data: dict, db_session: Session) -> dict:
        if not self.is_command_applicable(data):
            return data
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")
        print("Transforming data...")
        data['transformed'] = True
        return data
