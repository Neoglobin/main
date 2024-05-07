class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"The man, whose name {self.name} is walking")

man = Person("Vasya", 25)
man.walk()