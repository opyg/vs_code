class NewClass:
    def __init__(self, value):
        self.value = value
# te metody  pozwalają na zdefiniowanie reprezentacji tekstowej obiektów
    def __repr__(self):
        return f"NewClass({self.value})"
    def __str__(self):
        return f"Value: {self.value}"
    
object1 = NewClass(42)

print(repr(object1)) 
print(str(object1))  
print(object1) 

"""
Jeśli klasa implementuje zarówno __repr__ jak i __str__
print() korzysta z __str__ ale jeśli __str__ nie jest dostępne, używane jest __repr__.
W przypadku braku obu metod, używana jest domyślna reprezentacja obiektu, która obejmuje jego adres w pamięci.
"""
