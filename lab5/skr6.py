import math

def ladder_height(length: float, angle: float) -> float:
    height = length * math.sin(math.radians(angle))
    return round(height, 8)

l = float(input("Podaj długość drabiny: "))
a = float(input("Podaj kąt (w stopniach): "))

print(f"Wysokość wynosi: {ladder_height(l, a)}")