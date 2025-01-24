from typing import List, Dict
from Unit  import Unit 

class Connector:
    def __init__(self, *systems: Unit):
        self.systems: List[Unit] = list(systems)  # List of connected units

    def process(self, input_data: float) -> Dict[str, float]:
        outputs: Dict[str, float] = {}
        for system in self.systems:
            outputs[system.name] = system.process(input_data)
        return outputs
