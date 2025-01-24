from Connector import Connector
from typing import Dict 
class Coordinator:
    def __init__(self, connector: Connector):
        self.connector: Connector = connector

    def simulate(self, input_data: float, cycles: int) -> None:
        current_input: float = input_data
        for i in range(cycles):
            print(f"Cycle {i + 1}: Input = {current_input}")
            output: Dict[str, float] = self.connector.process(current_input)
            print("Output =", output)
            # Sum up all output values for feedback
            current_input = sum(output.values())
