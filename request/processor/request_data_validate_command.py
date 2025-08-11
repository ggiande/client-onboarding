from common.processor import ValidateCommandBase


class RequestDataValidateCommand(ValidateCommandBase):


    def __init__(self, service_name: str):
        super().__init__(service_name)
        self.service_name = service_name

    def is_command_applicable(self) -> bool:
        return True

    def execute(self, data: dict) -> dict:
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")

        print("Validating data...")
        if 'some_required_field' not in data:
            raise ValueError("Missing 'some_required_field'")
        data['validated'] = True
        return data