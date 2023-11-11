import math 
import random

def rand3()->tuple:
    a = random.randint(3, 10)
    b = random.randint(3, 10)
    c = random.randint(3, 10)
    return a, b, c

a,b,c = rand3()

print (a,b,c)
def chek(a,b,c)->bool:
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def calculate_area(a, b, c)->float:
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if(chek(a,b,c)):
    print("Yes")
    print(f'Area: {format(calculate_area(a,b,c), ".2f")}')
else:
    print("No")