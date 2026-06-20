# 02 Strings And Conditional Statements

print("02 Strings And Conditional Statements ")

str1 = "This is a string"
str2 = 'YK'
str3 = """This is "Third String" """
str4 = "This is a string. We are creating it in python"
str5 = "This is a string.\nWe are creating it in python"
str6 = "This is a string.\t We are creating it in python"
str7 = "We are creating it in python"
str8 = "Yashashvi Kochar"

#concatenation

final_str = str1 + " " + str7
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str1 + str7)
print(final_str)
print(len(final_str))
print(len(str6))

#index
print(str2[0])
print(str2[1])

#slicing
print(str8[0:9])
print(str8[10:16])
print(str8[:9])
print(str8[10:])

#slicing using negative index
print(str8[-6:])

#STRING FUNCTIONS

str9 = "My name is Yashashvi"
str10 = "I am a student"
str11 = "i am learning coding"
str12 = "i aspire to become an engineer"
str13 = str11.capitalize
str14 = "Map Cat Pat"

print(str9.endswith("vi"))
print(str10.endswith("vi"))
print(str12)
print(str12.capitalize())
print(str13)
print(str14.replace("a","o"))
print(str9.replace("Yashashvi","Yashashvi Kochar"))
print(str11.find("l"))
print(str12.find("become"))
print(str12.count("e"))

#practice

#1write a program to find the lenghth of name input 

#2 Write a program to find the occurence of '$' in a string

str15 = " This is $, $ is us symbol foe currency, 1$ = 94 rupees"
print(str15.count("$"))

# CONDITIONAL STATEMENTS

# if, elif, else

#if(condition) returns true or false

age = 14
if(age>= 18):
    print("Can vote and drive")
else:
    print("Cannot vote and drive")

#elif

light = "Green"
if(light == "Green"):
    print("Go")
if(light == "Red"):
    print("Stop")
if(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")

num = 7
if(num > 2):
    print("Greater than 2")
elif(num > 3):
    print("Greater than 3")

#PRACTICE
#Grade students based on thier marks

marks = int(input("Enter marks:"))

if(marks>=90):
    grade = "A"
elif(marks>= 80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
elif(marks>=60 and marks<70):
    grade= "D"
elif(marks>=50 and marks<60):
    grade= "E"
else: 
    grade = "F"    

print("Grade of the student is ", grade)

#NESTING

a = 98
if(a >= 18):
    if(a >= 80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")

#PRACTICE QUESTIONS

#1 Check if number entered by user is odd or even 

number = int(input("Enter the number-"))
remainder = number % 2

if(remainder == 0):
    print("The number is even")
else:
    print("The number is odd")

#2 find the greatest of 3 numbers entered

x = int(input("enter first number:"))
y = int(input("enter second number:"))
z = int(input("enter third number:"))

if(x >= y and x>=z):
    print("First number is largest", x)
elif(y >= z):
    print("Second is largest", y)
else:
    print("Third is largest", z)

#3 Check if a number is multiple of 7 or not

t = int(input("Enter your number:89"))
remainder = t % 7
if(remainder == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")

print("02END")

