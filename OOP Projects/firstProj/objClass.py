#Objected orientated programming in python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


d = Dog("Tim", 20)
print(d.name)
print(d.get_age())
d.set_age(5)
d.set_name("Paul")
print(d.get_name())
print(d.get_age())
d2 = Dog("Bill",34)
print(d2.name)
print(d2.get_age())
d2.set_age(10)
d2.set_name("Mark")
print(d2.get_name())
print(d2.get_age())
