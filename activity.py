class Car:
    def __init__(self, colour, brand, distance):
        self.colour = colour
        self.brand = brand
        self.distance = distance

    def disDis(self):
        print(f'The car has covered {self.distance} km')


car = Car('Red', 'Maruti', 300)
# car.disDis()

class Student:
    num = 0
    def __init__(self, name):
        self.name = name
    def average(self):
        total = 0
        for i in range(1,6):
            a = int(input(f'Enter the marks of subject {i}: \t'))
            total += a
        avg = total / 5
        self.num = total
        print(avg)
        
    def percentage(self):
        p = (self.num * 100) / 500
        print(p)


std = Student('A')
std.average()
std.percentage()