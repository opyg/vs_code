
# kek twowrzenie listy i sprawdzenie jej długości
my_list = [7,2,3,13,5]
print(my_list,"\nLength of list:" ,len(my_list))

# dodanie do listy różnych elementów
my_list[len(my_list):]= [40,20,'kot']
print(my_list)

# wyświetlam 2 pierwsze i 2 ostatnie elementy listy
print(my_list[:2], my_list[len(my_list)-2:])

# usunięcie ostatngo elementu bo on jest stringiem i sort() ne działa pomiędzy int i str ; sortowanie listy zwykłe i odwrotnie 
del my_list[len(my_list)-1]
list = sorted(my_list)
print("Sorted: ", list)
my_list.sort(reverse=True)
print("Reverse sorted:",my_list)

# dodanie elementu na miejsce o indeksie 2
my_list[2:2] = [1000]
print(my_list) 

# ile elementów w liście = 13
print("How much 13:",my_list.count(13))

# Prawie wszystkie operacje się udały
# elementy listy w Py są numerowane od 0 

