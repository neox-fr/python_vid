class Myclass: #defining a class
    x = 5 

p1 = Myclass()#odefining a object
print(p1.x)

# Create a class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}')

p1 = Person("John", 36)
p1.greet()

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} says Woof!')
    
d1 = Dog("Buddy", 3)
d1.bark()

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def show(self):
        print(self.brand)
    
c1 = Car("Ford")
c1.show()

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", 'A')
print(s1.grade)
s1.grade = "B"
print(s1.grade)

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r1 = Rectangle(5,3)
print(r1.area())

class Calculator:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a * b
    
calc = Calculator()
print(calc.add(5,3))
print(calc.multiply(4,7))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):#method used to return value when object is printed
        return f'{self.name} ({self.age})'
    
p1 = Person("Tobias", 36)
print(p1)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"added: {song}")

    def remove_song(self,song):
        if song in self.songs:
            print(f"Removed: {song}")
        
    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"-{song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()