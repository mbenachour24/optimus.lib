# Optimus SDK: A Toolkit for Modeling Institutional Interactions

## Introduction to the Optimus Method

The Optimus SDK is a Python-based framework designed to simulate and analyze institutional dynamics using principles derived from systems theory and computational modeling. This SDK embodies the four core pillars of the Optimus Method:

1. **Functional Differentiation**:
   Each institutional component (e.g., judiciary, executive, legislature) is modeled as an autonomous unit with a specific function.

2. **Autopoiesis**:
   Every unit operates independently, generating and maintaining its internal logic while interacting with other units.

3. **Structural Coupling**:
   Units interact through defined interfaces while preserving their autonomy, enabling stable yet dynamic interdependence.

4. **Orchestration**:
   A central `Coordinator` oversees system evolution, simulating iterative processes that reflect real-world institutional behavior over time.

## Project Structure

The SDK is structured to allow modular development and customization:

```
optimus_sdk/
|-- __init__.py          # Placeholder for package initialization (currently empty)
|-- Unit.py              # Defines the base class for all functional units
|-- ConnectableUnit.py   # Extends Unit with connectivity logic
|-- Connector.py         # Manages interactions between multiple units
|-- Coordinator.py       # Orchestrates the simulation process
|-- main.py              # Demonstrates basic usage of the SDK
```

## Installation

To use the Optimus SDK, clone the repository and ensure that your environment has Python 3.8+ installed:

```bash
git clone https://github.com/your-repo/optimus-sdk.git
cd optimus-sdk
pip install -r requirements.txt  # Include this if there are dependencies
```

## Getting Started

Here’s a quick guide to creating and running a simulation:

### Step 1: Define Units
Create custom units by extending `Unit` or `ConnectableUnit`. Each unit requires a name and a processing logic:

```python
from Unit import Unit

class JudicialUnit(Unit):
    def __init__(self):
        super().__init__("JudicialUnit", self.review_law)

    def review_law(self, law: str) -> str:
        return f"Reviewed: {law}"
```

### Step 2: Establish Connections
Use the `Connector` class to link units:

```python
from Connector import Connector
from JudicialUnit import JudicialUnit

judicial_unit = JudicialUnit()
connector = Connector(judicial_unit)
```

### Step 3: Simulate Interactions
Use the `Coordinator` class to run simulations:

```python
from Coordinator import Coordinator

coordinator = Coordinator(connector)
coordinator.simulate(input_data="New Law", cycles=3)
```

### Example Output
```plaintext
Cycle 1: Input = New Law
Output = {'JudicialUnit': 'Reviewed: New Law'}
Cycle 2: Input = Reviewed: New Law
Output = {'JudicialUnit': 'Reviewed: Reviewed: New Law'}
Cycle 3: Input = Reviewed: Reviewed: New Law
Output = {'JudicialUnit': 'Reviewed: Reviewed: Reviewed: New Law'}
```

## Contributing

We welcome contributions to improve the Optimus SDK! Please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, please reach out to [Mohamed Ben Achour](mailto:mbenachour24@gmail.com).

---
Start exploring the dynamics of institutional logic today with the Optimus SDK!
