
class Vehicle():
    def __init__(self, owner: str, table: str):
        self.owner = owner
        self.table = table

    def get_sound(self) -> None:
        print("vehicle's brum brum")

    def get_owner(self) -> str:
        return self.owner

class Car(Vehicle):
    def get_sound(self) -> None:
        print("car's brum brum")

car = Car("John", "A3")
vehicle = Vehicle("Alice", "X6")

car.get_sound() 
print(car.get_owner())  

vehicle.get_sound()  
print(vehicle.get_owner()) 



