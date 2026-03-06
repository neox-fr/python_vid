#inheritance

class Pet:#parent class
    def __init__(self,name, age):

        self.name = name
        self.age = age 

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print("what to say")

class Cat(Pet):#child classes
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and i am {self.color}')

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
c = Cat("bill", 34 , "orange")
c.show()
c.speak()
d = Dog("jill", 25)
d.show()
d.speak()
e = Fish("hell", 3)
e.speak() #since there is nothing defined inside the class Fish , the default is called from the parent class


