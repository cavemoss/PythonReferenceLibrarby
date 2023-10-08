class Animal:

    def __init__(self, string):
        self.species = string

    alive = True

    def eat(self):
        print(f'this {self.species} is eating')

    def sleep(self):
        print(f'this {self.species} is sleeping')


class Deer(Animal):

    def run(self):
        print('this deer is running')


class Bird(Animal):

    def fly(self):
        print('this bird is flying')


class Fish(Animal):

    def swim(self):
        print('this fish is swimming')


deer = Deer('deer')
deer.run()

bird = Bird('bird')
bird.fly()

fish = Fish('fish')
fish.swim()


print(deer.alive)
bird.eat()
fish.sleep()
