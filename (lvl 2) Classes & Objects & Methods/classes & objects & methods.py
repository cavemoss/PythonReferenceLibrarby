class Car:

    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f'the {self.make} {self.model} is driving', end='\n\n')

    def explode(self):
        print(f'the {self.make} {self.model} has been exploded', end='\n\n')

car_one = Car('Chevy', 'Corvette', 2019, 'blue')
car_two = Car('Ford', 'Mustang', 2020, 'red')

# instance one
print(car_one.make)
print(car_one.model)
print(car_one.year)
print(car_one.color)
car_one.drive()

# instance two
print(car_two.make)
print(car_two.model)
print(car_two.year)
print(car_two.color)
car_two.explode()

# instance three
print('a car normally has', Car.wheels, 'wheels')
car_one.wheels = 6
print(f'the {car_one.make} {car_one.model} now has', car_one.wheels, 'wheels')
Car.wheels = 6
print(f'the {car_two.make} {car_two.model} also has', car_two.wheels, 'wheels now')
