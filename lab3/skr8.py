
my_set = {1,24,'banana','fksdgks',4}
print(my_set)

try: 
    my_set.remove(24) 
    print(f"after remove: {my_set}")
except KeyError: 
    print('element does not exist') 

try: 
    my_set.discard(5) 
    print(f"after discard: {my_set}")
except KeyError: 
    print('element does not exist')

# różnica pomiędzy remove() a discard() jest w tym że jeśli 
# takiego elementu nie ma w zbiorze to remove wyłołuje ERROR a discard nie
print(my_set)
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
#zawsze jest zdejmowany pierwszy element(z indeksem 0, chociaż tutaj je nie ma) 