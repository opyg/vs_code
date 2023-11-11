class Item:
    def get_sound(self) -> None:
        print("item's sound")
class Element:
    def get_sound(self) -> None:
        print("element's sound")
class Thing(Item,Element):
    def say_hello(self) -> None:
        print("hello!")

"""

"""


i = Item()
i.get_sound()

e = Element()
e.get_sound()

t = Thing()
t.get_sound()