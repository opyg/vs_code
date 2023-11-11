class NewClass:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def sum(self)->int:
        return self.x + self.y

o = NewClass(1, 2)

print(o.__dict__) 

o.__dict__['x'] = 10
print(o.x)  

print(NewClass.__dict__)


