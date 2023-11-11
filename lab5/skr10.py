import math
import platform
import sys

a = float(input("give the number a: "))
b = int(input("give the number b: "))

def testowanief(a,b):
    print(math.trunc(a))
    print(math.floor(a))
    print(math.ceil(a))

    print(sys.version_info)
    if sys.version_info > (3, 9):
        print(math.lcm(int(a),b)) #najmniejsza wspólna wielokrotność
        print(math.gcd(int(a),b)) #największy wspólny dzielnik
    # Obliczanie wartości bezwzględnej
    print(f'Wartość bezwzględna: {math.fabs(a)}')
    
if __name__ == "__main__":
    testowanief(a,b)
