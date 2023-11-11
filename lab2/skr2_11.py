

a:float = 2
b:float = 5 
c:float = 10

#a
d = c/a
if c/a/b == d/b : 
    print("a)od lewej")
else: 
    print("a)od prawej")

#b
if a*b+c == c+a*b: 
    print("b)mnozenie")
else: 
    print("b)dodawanie")
#c 
if (a*b)+c == a*(b+c):
    print("c)nie wplywaja")
else: 
    print(f"c)wplywaja: {(a*b)+c} i {a*(b+c)} to rozne") 
#d
if a**b*c < c*a**b: 
    print("d)mnozenie")
else: 
    print("d)potegowanie")