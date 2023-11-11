
from math import pi
def main():
    r = input("Podaj promien:\n")
    pole = pi*float(r)**2

    obwod =2*pi*float(r)
    print("Pole:", pole ,"\nObwod:", obwod)
    pass
if __name__ == '__main__':
    main()