from request.processor.command import Command


class RequestSendCommand(Command):
    def is_telemetry_turned_on(self):
        pass

    def handle_exception(self):
        pass

    def handle_command_execution_exception(cls):
        pass

    def get_event_region_name(self):
        pass

    def post_process(self):
        pass

    def __init__(self, service_name: str):
        self.service_name = service_name

    def execute(self, data: dict) -> dict:
        print("Sending the request...")
        # Simulate an external call
        data['sent'] = True
        return data