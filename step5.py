#loops

#while loop
condition = True 
while condition == True: # repeat as long as its true
    print("the condition is true")
    condition = False

count = 0
while count < 10:
    print("the world")
    count += 1
print("after loop")

#for loop

items = [1,2,3,5]
for index, item in enumerate(items):
    print(item, index)
for item in range(15):
    print(item)

for item in items:
    for item in items:
        if item == 2:
            continue # if break it just stops and doesnt go to the print below
        print(item)

#lambda functions

lambda num : num * 2

multiply = lambda a,b : a * b
print(multiply(2,4))

#map(), filter(), reduce()

numbers = [1,2,3]
def double(a):
    return a *2
result = map(double, numbers)
print(list(result))

def isEven(n):
    return n % 2 == 0
result = filter(isEven, numbers) 
result = filter(lambda n: n%2 == 0, numbers)
print(list(result))

expenses = [('dinner', 80),('car repair', 120)]
sum = 0
for expense in expenses:
    sum += expense[1]

#instead
from functools import reduce
expenses = [('dinner', 80),
    ('car repair', 120)]
sum = reduce(lambda a,b: a[1] + b[1], expenses)

print(sum)

#classes  


class Animal:
    def walk(self):
        print("Walking....")

class Dog(Animal):
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    
    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)
print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

from python_videos import module1
module1.bark()#or

from python_videos.module1 import bark
bark()