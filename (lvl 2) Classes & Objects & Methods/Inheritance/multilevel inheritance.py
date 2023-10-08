class Organism:
    alive = True


class Creature(Organism):

    def eat(self):
        print('this creature is eating')


class Cat(Creature):
    
    def meow(self):
        print('this cat is meowing')


kitty = Cat()

print(kitty.alive)
kitty.eat()
kitty.meow()
