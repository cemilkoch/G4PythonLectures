# Creating a class

class Things:
    pass


# Creating Inanimate Class
class Inanimate(Things):
    pass


# Creating Animate Class
class Animate(Things):
    pass


# Creating a subclass of inanimate
class Tree:
    pass


# Creating a subclass of Animate
class Animals(Animate):

    def eat(self):
        print("Eating")

    def breathe(self):
        print("Breathing")


class Mammals(Animals):

    def eat(self):
        print("Mammals feed with milk")


class Dogs(Mammals):

    def bark(self):
        print("Barking")


class Cats(Mammals):

    def speak(self):
        print("Meow")


reginald = Dogs()  # Dogs reginald = new Dogs(); Java
reginald.eat()

harold = Cats()  # Cats harold = new Cats(); Java
harold.speak()



