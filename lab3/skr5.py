
def double(a:list,b:list)->None:
        c:list = b +a
        print(c)
        c:list = a + b
        print(c)
pass

a:list = ['cat',12.1,-5]
b:list = [0,'dog', -9.2]
double(a,b)

