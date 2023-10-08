class Car:
    
    def turn_on(self):
        print('you start the car')
        return self

    def drive(self):
        print('you drive the car')
        return self
    
    def brake(self):
        print('you stop the car')
        return self
    
    def turn_off(self):
        print('you turn off the car')
        return self


the_car = Car()
the_car.brake().drive().turn_on().turn_off()
