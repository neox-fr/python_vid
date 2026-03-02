#Object Oriented Programming

def hello():
    print("hello")

print(type(hello)) #whatever we work with is already a pre defined class

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Tim",3) #creating a object
print(d.get_name())
print(d.get_age())
d.set_age(5)
print(d.get_age())
d2 = Dog("Bill",4)
print(d2.get_name())
print(d.get_age())
print(type(d)) #the object is printed as class dog



