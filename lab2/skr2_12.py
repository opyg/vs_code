

def foo():
   print(a/b,type(a/b))
   print(a//b,type(a//b))
   print(a%b,type(a%b),'\n')
   pass
# liczby calkowite 
a = 6
b = 2
foo()
# liczba calkowita i zminnoprzecinkowa
a = 7
b = 2.5
foo()
# liczby zmiennoprzecinkowe
a = 5.5
b = 0.5
foo()