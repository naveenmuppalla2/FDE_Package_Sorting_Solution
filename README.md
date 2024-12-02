# FDE Package Sorting Solution

## Objective
This repository contains the solution for sorting packages into appropriate stacks based on their volume and mass as specified in the FDE Technical Screen.

## Sorting Logic

The function `sort(width, height, length, mass)` determines the correct stack for a package based on the following rules:

1. **Definitions**:
   - **Bulky**:
     - Volume (width × height × length) ≥ 1,000,000 cm³, OR
     - Any dimension (width, height, or length) ≥ 150 cm.
   - **Heavy**:
     - Mass ≥ 20 kg.

2. **Stack Assignment**:
   - **STANDARD**: Neither bulky nor heavy.
   - **SPECIAL**: Either bulky or heavy (but not both).
   - **REJECTED**: Both bulky and heavy.

## Example Usage

### Function Definition
```python
def sort(width, height, length, mass):
    # Function logic here
    pass
