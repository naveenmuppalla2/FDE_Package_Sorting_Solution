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
print(sort(100, 50, 200, 15))  # STANDARD
print(sort(200, 200, 200, 10))  # SPECIAL (bulky)
print(sort(100, 50, 100, 25))  # SPECIAL (heavy)
print(sort(200, 200, 200, 30))  # REJECTED (both bulky and heavy)
