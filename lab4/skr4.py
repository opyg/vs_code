from typing import List

class Student:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.marks = []

    def _check_name(self, name: str, last_name: str) -> bool:
        return bool(name.strip() and last_name.strip())
# strip()jest używana do usunięcia białych znaków z początku i końca stringa 
# w tym kodzie sprawdza czy jest to pusty string(czyli składa się tylko z białych znaków lub są całkowicie pusty)
    def give_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name

    def give_mark(self, mark: int) -> None:
        self.marks.append(mark)

    def get_marks(self) -> List[int]:
        return self.marks

    def say_hello(self) -> None:
        if self._check_name(self.name, self.last_name):
            print("Hello! I'm " + self.name + " " + self.last_name)
        else:print("You have not name OR last name")


s = Student()
s.give_name("Jane", "Doe")
s.say_hello() 

s.give_name("", "Smith")
s.say_hello() 
