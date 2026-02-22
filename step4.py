#functions

def hello():
    print('hello')
hello()#calling a function

def nepal(name): #passing parameters
    print('hello' + name)
nepal('niraj')

def nepal(name="my friend"): #default value if no value is passed
    print("hello" + name)
nepal()

def change(value): #value inside wont change outside
    value = 3
val = 1
change(val)
print(val)

def change(value):
    value['name'] = 'sid' #a dict is prone to change
val = {"name": "beau"}
change(val)
print(val)

def change(name):
    print('hello'+ name + 'hey')
    return #ends the function

def test(a,b):
    if b > 2:
        if a > 1:
            return
        else:
         print("hello")
    else:
        print("nepal")
    print("nepal")
print(test(4,5))

#nested function

def talk(phrase):
        def say(word):#not going to be using outside the function
             print(word)
        words = phrase.split(' ')
        for word in words:
             say(word)
talk('I am going to buy the milk')

def count():
        count = 0
        def increment():
            nonlocal count
            count = count + 1
            print(count)

        increment()
count()