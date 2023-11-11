
def get_base()->int:
    while True:
        base = int(input('Podaj podstawę systemu liczbowego (2, 8, 10, 16): '))
        if base in [2, 8, 10, 16]:
            return base
        else:
            print('Podano nieprawidłową wartość!')

def convert_and_print(base)->None:
    num = int(input('Podaj liczbę: '), base)
    print('Dwójkowy:', bin(num))
    print('Ósemkowy:', oct(num))
    print('Dziesiętny:', num)
    print('Szesnastkowy:', hex(num))

convert_and_print(get_base())