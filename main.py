from System import System
from typing import List
import random


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


judicial_unit = System(
    "judicial", 
    {
        "produce_case": produce_case, 
        "review_law": review_law
     })

def produce_law():
    return "you shall not kill " + random.choice(["humans", "ducks", "fish"])

political_unit = System("political", {"produce_law": produce_law})

political_unit.process("produce_law")
political_unit.process("produce_law")
laws = political_unit.get_state()

print(laws)

judicial_unit.process("produce_case", laws, "Mohamed killed an alien")
cases = judicial_unit.get_state()
print(cases)
political_unit.process("produce_law")
laws = political_unit.get_state()["produce_law"]
latest_law = laws[-1]
judicial_unit.process("review_law", latest_law)
print(judicial_unit.get_state())
