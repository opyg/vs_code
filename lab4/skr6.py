class Student:
    def __init__(self, name:str, last_name:str, index:int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __lt__(self, other)->bool:
        return self.index < other.index

    def __gt__(self, other)->bool:
        return self.index > other.index

    def __eq__(self, other)->bool:
        return self.index == other.index

    def __le__(self, other)->bool:
        return self.index <= other.index

    def __ge__(self, other)->bool:
        return self.index >= other.index

    def __ne__(self, other)->bool:
        return self.index != other.index


s1 = Student("Jan", "Kowalski", 121345)
s2 = Student("Bob", "Marley", 122890)

print("s1 < s2:", s1 < s2)  
print("s1 > s2:", s1 > s2)  
print("s1 == s2:", s1 == s2)
print("s1 <= s2:", s1 <= s2)
print("s1 >= s2:", s1 >= s2)
print("s1 != s2:", s1 != s2)

