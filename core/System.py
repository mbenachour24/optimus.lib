from typing import Callable, List, Dict
import random

colors = [31, 32, 33, 34, 35, 36, 37]  # Red, Green, Yellow, Blue, Magenta, Cyan, White

class System:
    class Coupling:
        def __init__(self, func: Callable, connection: 'System'):
            self.connection = connection
            self.func = func

    def __init__(self, name: str, logics: Dict[str, Callable]):
        self.name: str = name
        self.logics: Dict[str, Callable] = logics
        self.state: Dict[str: List[str]] = {}
        self.couplings: List['System.Coupling'] = []
        self.color = random.choice(colors)

    def get_state(self) -> Dict[str, List[str]]:
        """Returns the current state of the system."""
        return self.state
    
    def process(self, process_name: str, *args, **kwargs) -> str:
        """Executes a logic process and updates the system state."""
        print(f"\033[{self.color}m{self.name} processing {process_name}\033[0m")
        if process_name not in self.logics:
            raise ValueError(f"Process {process_name} is not defined in logics.")
        result = self.logics[process_name](*args, **kwargs)
        self.state.setdefault(process_name, []).append(result)
        return result
    
    def add_coupling(self, func: Callable, unit: 'System'):
        """Creates a coupling with another system."""
        coupling = System.Coupling(func, unit)
        self.couplings.append(coupling)

        