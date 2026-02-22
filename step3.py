#About list, dict, tuples, sets

#lists
dogs = ["roger", 1, True] #can mix data types
print("Beau" in dogs) #in checks if available or not
print(dogs[0]) #prints the specific data in the list
dogs[0]= "nepal" #changes the value in the list
print(dogs[1:3]) #specific part
dogs.append("hello")#adds single data to the list at the end
print(dogs)
dogs.extend(["judah", 5]) #multiple append
print(dogs)
dogs += ["judah", 5] #sames as extend
dogs.remove("nepal")
print(dogs)
print(dogs.pop()) #removes the last one in the list and prints it
dogs.insert(2, "test") #adds to the list at a specific part
dogs[1:1]=["test1","test2"] #adding multiple using slices
items = ["nepal","China","usa"]
items.sort()#sorts the list (alphabet included)
print(items)
print(sorted(items, key=str.lower)) #prints the list without changing the original one
items.sort(key=str.lower)
print(items)
itemscopy= items[:] #copying the list
print(itemscopy) 

#Tuples
names = ("roger", "syd") # a tuple cant be modified
names[0]
names.index("roger")
print(names[:]) #prints the whole list
print(sorted(names)) #sort alphabetically but cant modify it
newTuple = names + ("hello", "nepal") #can add to a new one
print(newTuple)

#Dictionaries

auto = {"name": "Roger", "age": 20}
print(auto['name'])
auto["name"] = "sam" #changing value
print(auto)
print(auto.get("name")) #also to get a specific value
print(auto.get("color", "brown")) #if there is no data it can be used to add default values
print(auto.pop("name")) #gets the item and remove from dict
print("color" in auto)
print(auto.keys()) #the keys only in a dict
print(auto.values()) # only the value
print(list(auto.values()))# passes the value to a list
print(len(auto))
auto["fav food"] = "meat"
print(auto)
del auto['fav food'] #deletes both value and key
print(auto)
autocopy = auto.copy()

#sets
 
set1= {"roger","nepal"} #set cant have same value
set2= {"roger"}
mod = set1 & set2 #intersect in set
mod = set1 | set2 #union in set
mod = set1 - set2 #difference in set
mod = set1 > set2 #checks if one set has everything of the other
print(mod)
print(list(set2))

print("nepal" in set1)