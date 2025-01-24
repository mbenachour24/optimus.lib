from Unit import Unit
from ConnectableUnit import ConnectableUnit

class JurdicalUnit(Unit):
    pass


class PoliticalUnit(ConnectableUnit):
    def connect(self, unit: JurdicalUnit):
        unit.process(self.state[0])

def review_law(law: str) -> str:
    result = f"review law: {law}"
    print(result)
    return result

def reform_law(law: str) -> str:
    result = f"reform law: {law}"
    print(result)
    return result

ju = JurdicalUnit("JurdicalUnit", review_law)
pu = PoliticalUnit("PoliticalUnit", reform_law)

if __name__ == "__main__":
    print("Hello! this is Optimus 🦾")
    pu.process("1st amendment")
    pu.process("2nd amendment")
    pu.connect(ju)
