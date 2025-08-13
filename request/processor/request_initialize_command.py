from common.processor.initialize_command_base import InitializeCommandBase
from exception import RequestDataValidationException

class RequestInitializeCommand(InitializeCommandBase):

    def __init__(self, service_name: str):
        self.service_name = service_name

    def is_command_applicable(self) -> bool:
        pass

    def execute(self, data: dict) -> dict:
        """
        assert source, assert format, assert number of entries to be processed in the batch,
        brand name, isPartnerBrand, status, hasExceptions
        :param data:
        :return:
        """
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")

        errors = {}


        if "username" not in data or not isinstance(data["username"], str):
            errors.setdefault("username", []).append("Username must be a string.")
        if "age" not in data or not isinstance(data["age"], int) or data["age"] < 18:
            errors.setdefault("age", []).append("Age must be an integer 18 or older.")

        if errors:
            raise RequestDataValidationException(errors)

        print("Initializing the request...")
        data['initialized'] = True
        return data
