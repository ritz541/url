class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof")

d = Dog('Tommy')
d.bark()


