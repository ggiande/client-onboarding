from common.processor import TransformCommandBase


class RequestTransformCommand(TransformCommandBase):

    def is_command_applicable(self) -> bool:
        pass

    def __init__(self, service_name: str):
        self.service_name = service_name

    def execute(self, data: dict):
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")
        print("Transforming data...")
        # data['transformed'] = data['some_required_field'].upper()

