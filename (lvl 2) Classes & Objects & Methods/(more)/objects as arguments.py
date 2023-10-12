class Car:
    color = None


class Motorcycle:
    color = None  


car_one = Car()
car_two = Car()
car_three = Car()
bike_one = Motorcycle()


def change_color(vehicle, color):
    vehicle.color = color

change_color(car_one, 'red')
change_color(car_two, 'white')
change_color(car_two, 'blue')
change_color(bike_one, 'black')

print(car_one.color)
print(car_two.color)
print(car_three.color)
print(bike_one.color)
