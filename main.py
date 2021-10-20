class Dog:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed 
        self.colour = colour

    def sound(self):
        print(self.name, "Bhow Bhow!")

a = Dog('Dog','Germen Shapherd', 'Black')
a.sound()
print(a.colour)
