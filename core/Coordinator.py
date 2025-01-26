
from abc import abstractmethod
from typing import Dict
from System import System


class Coordinator:
    def __init__(self, systems: Dict[str, System]):
        self.systems = systems
    def add_system(self, system: System):
        self.systems[system.name] = system
    def remove_system(self, system_id: str):
        del self.systems[system_id]
    @abstractmethod
    def simulate(self):
        pass