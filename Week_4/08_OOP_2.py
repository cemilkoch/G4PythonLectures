# Naming the class usually is UpperCase
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def bark(self):
        print(self.name, "is barking")


bob = Dog("Bob", 6)  # Dog bob = new Dog("Bob");
bob.eat()
bob.bark()
print(bob.name)
print(bob.age)



