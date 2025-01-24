from abc import ABC, abstractmethod
from typing import Callable, List
from Unit import Unit

class ConnectableUnit(Unit):
    @abstractmethod
    def connect(self, unit: 'Unit'):
        pass
