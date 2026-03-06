
class Person:
    number_of_people = 0 #specific to class

    def __init__(self, name):
        self.name = name

p1 = Person("tim")
p2 = Person("jill")

Person.number_of_people = 8 # is specific to class not to instances so can be changed
print(p1.number_of_people)