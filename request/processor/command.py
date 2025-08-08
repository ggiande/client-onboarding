from abc import ABC, abstractmethod
class Command(ABC):

    @abstractmethod
    def execute(self, data: dict):
        pass

    @abstractmethod
    def handle_exception(self):
        pass

    @abstractmethod
    def handle_command_execution_exception(cls):
        pass

    @abstractmethod
    def is_telemetry_turned_on(self):
        pass

    @abstractmethod
    def get_event_region_name(self):
        pass

    @abstractmethod
    def post_process(self):
        pass