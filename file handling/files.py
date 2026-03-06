
f= open("file.txt","x") #creates a new file

f = open("file.txt") #opens the file from the system
print(f.read()) #reads
f.close() #closing the file if no with

#f = open("D:\\myfiles\welcome.txt") #specific location
#print(f.read(5)) # can specify how much character u want to read

with open("file.txt") as f:
    print(f.readline()) #reads a single line
    print(f.readline()) #recalling makes it 2 lines

with open("file.txt", "a") as f: 
  f.write("Now the file has more content!") #adding

with open("file.txt", "w") as f:
  f.write("Woops! I have deleted the content!") #overwriting

with open("file.txt") as f: #reads the whole file line by line, memory efficient
  for x in f:
    print(x)

import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")

#import os
#os.rmdir("myfolder")