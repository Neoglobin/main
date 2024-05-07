class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"The man, whose name {self.name} is walking")


class Face(Person):
    def __int__(self, name, age, face):
        super().__init__(name, age)
        self.face = face

    def smile(self):
        if self.face == True:
            print(f"{self.name} is getting an emotion like - :)")

man = Person("Vasya", 25)
man.walk()
another_man = Face("Alyosha", 30, True)
another_man.smile()