class Student:
    quantity = 0
    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.marks = []
        Student.quantity += 1

s1 = Student()
print(s1.quantity)
s2 = Student()
print(s2.quantity)
s3 = Student()
print(s3.quantity)
s4 = Student()
print(s4.quantity)
print(s1.quantity)
print(s2.quantity)
print(Student.quantity)
"""
 ta zmienna quantity jest zmienną klasy a dla każdego jej objektu jest taka sama 
 (jakby była self.quantity w funkcji init to dla każdej instancji była by swoja) 
"""