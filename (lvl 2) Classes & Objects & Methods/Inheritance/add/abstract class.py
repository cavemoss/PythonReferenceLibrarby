from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print('you drive the car')

    def stop(self):
        print('you stopped the car')


class Motorcycle(Vehicle):

    def go(self):
        print('you drive the motorcycle')

    def stop(self):
        print('you stopped the motorcycle')


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

# vehicle.stop()
car.stop()
motorcycle.stop()
