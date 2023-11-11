def power_of_two(p: int):
    if p > 0:
        return 1 << p
    elif p == 0:
        return 1
    else:
        print("Wykładnik potęgi nie może być ujemny")

if __name__ == "__main__":
    try:
        p = int(input("Podaj wykładnik potęgi: "))
        print(power_of_two(p))
    except ValueError:
        print("Podana wartość nie jest liczbą całkowitą!")
