class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

man = Person("Vasya", 25)
print(man.name + " " + str(man.age))
