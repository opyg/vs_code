
x = {1,2,3,4}
y = {2,5,6,7}

print(x.isdisjoint(y))
#sprawdza czy są wspólne elementy
print(x.issubset(y))
#czy zbior x jest podzbiorem y
print(x.issuperset(y))
#czy zbior x jest nadzbiorem y
print(x.union(y))
#suma zbiorów
print(x.difference(y))
#różnica zbiorów
print(x.intersection(y))
#przecięcie zbiorów