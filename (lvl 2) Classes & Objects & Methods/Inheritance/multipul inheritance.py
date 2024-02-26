class Prey:

    def flee(self):
        print('this animal flees')


class Preditor:

    def hunt(self):
        print('this animal is hunting')


class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

class Fish(Prey, Preditor):
    pass


abby = Rabbit()
hawky = Hawk()
fishy = Fish()

abby.flee()
hawky.hunt()

fishy.hunt()
fishy.flee()
