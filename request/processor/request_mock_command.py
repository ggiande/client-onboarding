from common.processor import MockCommandBase


class RequestMockCommand(MockCommandBase):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def is_command_applicable(self) -> bool:
        pass

    def execute(self, data: dict) -> dict:
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")
        print("Mocking a command...")
        data['mocked'] = True
        return data
