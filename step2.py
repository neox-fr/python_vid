name = "beau" #assigning value to a variable
print(name) #print value
#this is a comment
#indentation matters in python
print(type(name)) #shows the type of the variable
print(type(name)==str) # checking if variable is true or false
print(isinstance(name, str)) #checks whether an object or variable is an instance of a type or class
age= float(2)
print(isinstance(age, float))
age="20"
print(isinstance(age, int))
age=int("20") #casting , converting to another data type
print("hello"+"world") #adding strings
print(f"hello, name is {name} and i am {age} ") #also used to add strings
print(0 or 1) #doesnt return false value, applies to false [] null
print(False or []) #returns second value
def is_adult(age):
    if age >18:
        return True
    else:
        return False
print(is_adult(age)   )
def is_adult2(age):
    return True if age > 18 else False #using ternary operator
print(is_adult2(age))
name = "gagan "
name += "is my name"
print(name)
print("""hello
my 
name is 
gagan""") #multi line string
print("beau".upper())
print("beau".lower()) #uppercase and lowercase
print("beau".title()) #makes first letter capital
print(name.islower())
print("person".islower()) #checks condition
global a #global variable
print(len(name)) #checks how many alphabets
print("my" in name)
name = "hello \"nepal" #\ to escape character
print(name[0]) #print first character as its 0
print(name[1:5]) #starts from 1 to 5 (includes 5)
print(name[:5]) #prints from beginning
done= True #if string and is not empty, also is considered true
print(bool(done))#checks boolean

if done:
    print(name)
else:
    print("no")

book_1= True
book_2= False
read= any(
[book_1, book_2]
) #if any one is true
print(read)
read= all(
[book_1, book_2]
) #only if all is true
print(read)
num=complex(2,3) #converts to complexs
print(num)
print(abs(-5.5)) #returns absolute value
print(round(5.5)) #rounds to the nearest 
print(round(5.5545,2)) #can specify floating value
nepal = 1
if nepal == 1:
    print("hello")
elif nepal ==0:
    print("no")
else:
    print("error") #condition

from enum import Enum

class State(Enum):
    Inactive=0
    Active=1
print(State.Active.value)
print(list(State)) #list the value inside the class
age =input("what is ur name") #inputs value to variable