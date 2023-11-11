
tuple1 = ("apple", "banana", "cherry") #stworzenie krotki
print (tuple1[0]) # wypisanie elementu z indeksu 0
print (tuple1) # wypisanie krotki
nested_tuple = tuple1, (1,2,3,4,5) # definiowanie zagnieżdżonej krotki
print(nested_tuple)

tuple1 = ("apple", "banana", "cherry")
tuple_b = ("orange",)

tuple1 += tuple_b #dodawanie krotek
print(f"after adding:{tuple1}")
tuple1 += tuple1
print(f"sama do siebe:{tuple1}")
multi_tuple = tuple1 * 2 #mnożenie krotek
print(multi_tuple)
print(len(tuple1)) #długość krotki - liczba elementów
for x in tuple1: #wypisanie wszystkich elementów krotki
    print(x)
sorted_tuple = sorted(tuple1)
print(sorted_tuple)