

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} year(s) old")
    
    def grow_up(self, years):
        self.age = self.age + years



mikey = Person("Michael Diner", 14)
aj = Person("Aiden Diner", 12)

people = []


people.append(mikey)
people.append(aj)

people.append(Person("Igor", 44))

for p in people:
    p.say_hello()




