def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
# Test cases
print(sort(100, 50, 200, 15))  # STANDARD
print(sort(200, 200, 200, 10))  # SPECIAL (bulky)
print(sort(100, 50, 100, 25))  # SPECIAL (heavy)
print(sort(200, 200, 200, 30))  # REJECTED (both bulky and heavy)
# Edge cases
print(sort(150, 150, 150, 19))  # SPECIAL (bulky)
print(sort(149, 149, 149, 20))  # SPECIAL (heavy)
print(sort(150, 150, 150, 20))  # REJECTED (both bulky and heavy)
print(sort(149, 149, 149, 19))  # STANDARD
print(sort(100, 50, 20, 1))     # STANDARD (small and light)
print(sort(300, 50, 10, 25))    # SPECIAL (bulky)
print(sort(1000, 1000, 1, 19))  # SPECIAL (bulky)
