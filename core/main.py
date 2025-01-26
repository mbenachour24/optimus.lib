from System import System
from Coordinator import Coordinator
from typing import List, Dict
import random
import time

def produce_case(laws: List[str], case: str):
    status = random.choice(["guilty", "not guilty"])
    print("processing case", case, " with laws:", laws)
    return {
        "case": case,
        "status": status
    }

def review_law(law: str):
    status = random.choice(["constitutional", "unconstitutional"])
    print("processing case", law)
    return {
        "law": law,
        "status": status
    }

def produce_law():
    return "you shall not kill " + random.choice(["humans", "ducks", "fish"])

class SocietyCoordinator(Coordinator):
    def __init__(self, systems: Dict[str, System], people: List[str]):
        super().__init__(systems)  # Corrected the call to the parent constructor
        self.people = people
        
    def simulate(self):
        # Produce laws using the political unit
        political_unit = self.systems["political"]
        political_unit.process("produce_law")
        political_unit.process("produce_law")
        laws = political_unit.get_state()["produce_law"]
        print("Produced Laws:", laws)

        # Process a case using the judicial unit
        judicial_unit = self.systems["judicial"]
        random_killer = random.choice(self.people)
        judicial_unit.process("produce_case", laws, f"{random_killer} killed an alien")
        cases = judicial_unit.get_state()["produce_case"]
        print("Processed Cases:", cases)

        # Produce another law and review it
        political_unit.process("produce_law")
        latest_law = political_unit.get_state()["produce_law"][-1]
        judicial_unit.process("review_law", latest_law)
        print("Reviewed Law:", judicial_unit.get_state()["review_law"])
        time.sleep(10)
        self.simulate()

# Create the systems
judicial_unit = System(
    "judicial", 
    {
        "produce_case": produce_case, 
        "review_law": review_law
     })

political_unit = System("political", {"produce_law": produce_law})

# Create the coordinator and add the systems
coordinator = SocietyCoordinator({
    "political": political_unit,
    "judicial": judicial_unit
}, ["Mohamed", "Tawfik", "Kais Saied"])

# Run the simulation
coordinator.simulate()