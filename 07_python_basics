# FILE INPUT/OUTPUT
# Used to perform actions on a file (Read and Write)

# r reading a file 

f = open("Aircraft_telemetry.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("Aircraft_telemetry.txt", "r")
data = f.read(29)
print(data)
f.close()

# gives same output
f = open("Aircraft_telemetry.txt", "r")
line1 = f.readline()
print(line1)
f.close()

f = open("Aircraft_telemetry.txt", "r")
line9 = f.readline()
print(line9)
f.close()

# gives different output
f = open("Aircraft_telemetry.txt", "r")

line1 = f.readline()
print(line1)

line9 = f.readline()
print(line9)

f.close()


# x create new file and open to write
#b for binary file written as rb,ra
#t for text file default
# + to update 

# w deletes whole data and then overwrite
# f = open("College_list.txt", "w")
# f.write("I want to go in following colleges:DAIICT,PDEU,LD,VGEC,GEC,LJ,LDRP.")
# changes whole file 
# f.close()

# a add new data in existing one
f = open("College_list.txt", "a")
f.write("\nI want any of the following branches:ECE,ICE,EIE,IE or Electrical")
f.write("\nI want to further go for masters degree in Aerospace Engineering")
f.close()

# if a file does not exist a new file gets created
f = open("Myself.txt", "a")
f.close()

# # r+ to overwrite in beginning
# f = open("Myself.txt", "r+")
# f.write("I am")
# print(f.read())
# f.close()

# with syntax

with open("Myself.txt", "r") as f:
    data = f.read()
    print(data)

with open("Myself.txt", "w") as f:
    f.write("new data")

import os 
os.remove("Myself.txt")

# Practice problems

# Create a new file and replace a word with another

with open("Practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)
# Output changed to python

with open("Practice.txt", "w") as f:
    f.write(new_data)
# Name changed in txt file

# to check if a word exists in file 

word = input("Enter word to find:")
with open("Practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):            
        print("Found")
    else:
        print("Not found")

# to check in which line a word exists 
word = input("Enter the word:")
def check_for_line():
    data = True
    line_no = 1
    with open("Practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
   
    return -1 
    
print(check_for_line())

# from a file containing numbers seperated by comma, print count of even numbers

count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

    


