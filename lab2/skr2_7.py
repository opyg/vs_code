
import math
def main():
    print("Podaj wspolczynnuki:")
    a = float(input())
    b = float(input())
    c = float(input())
    print(a,b,c)
    x1 = (-b - (math.sqrt(b*b - 4*a*c)))/2   
    x2 = (-b + (math.sqrt(b*b - 4*a*c)))/2 
    print( x1, x2)
    pass
if __name__ == '__main__':
    main()