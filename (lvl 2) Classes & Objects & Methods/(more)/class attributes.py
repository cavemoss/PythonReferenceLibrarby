class Person:

    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def how_many_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

person_one = Person('Ron')
person_two = Person('Billy')

print(Person.number_of_people)
print(Person.how_many_people())
