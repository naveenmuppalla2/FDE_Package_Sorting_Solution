# FDE Package Sorting Solution

# Objective
This repository contains the solution for sorting packages into appropriate stacks based on their volume and mass.

# Sorting Logic:
1. **STANDARD**: Packages that are neither bulky nor heavy.
2. **SPECIAL**: Packages that are either bulky or heavy.
3. **REJECTED**: Packages that are both bulky and heavy.

# Usage
The function 'sort(width, height, length, mass)' takes the following parameters:
- 'width', 'height', 'length' (in cm): Dimensions of the package.
- 'mass' (in kg): Weight of the package.

# Example:
python
print(sort(100, 50, 200, 15))  # Output: "STANDARD"
