from abc import ABC
from typing import Callable, List

class Unit(ABC):
    def __init__(self, name: str, logic: Callable[[str], str]):
        self.name: str = name
        self.logic: Callable[[str], str] = logic
        self.state: List[str] = []

    def process(self, input_data: str) -> str:
        el = self.logic(input_data)
        self.state.append(el)
        return el
