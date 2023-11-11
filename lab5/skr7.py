import math as m

def check_one():
    for angle in range(91):
        a_r = m.radians(angle)
        result = round(m.sin(a_r)**2 + m.cos(a_r)**2, 5)
        print(f"Kąt: {angle} stopni, wynik: {result}")
        if result != 1:
            print(f"Jedynka trygonometryczna nie sprawdza się dla kąta {angle} stopni. Wynik: {result}")
check_one()