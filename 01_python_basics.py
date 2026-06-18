print("Yashashvi Kochar")

#basics

print("My name is Yashashvi Kochar")
print("My age is 18 years")
print("My name is Yashashvi Kochar","My age is 18 years")
print(18)
print(18+17)

name = "Yashashvi Kochar"
age = 18
Education = "Grade twelve"
print("My name is:",name)
print("My age is:",age)
print("I have complted",Education) 
score=70.5
print(type(name))
print(type(age))
print(type(score))

name1='Yashashvi'
name2="Yashashvi"
name3='''Yashashvi'''

print(name1,name2,name3)

old=True
y=None
print(type(old))
print(type(y))

a=18
b=17
sum=a+b
difference=a-b
print(sum)
print(difference)

print("Hello")
#print("Hello")
# this is a comment
"""
this is again a comment
even this is another comment
"""
print("Hello World")

# print("Hello World")
# print("Hello World")
# print("Hello World")

print("World")

#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a % b)

#relational/comparision operators
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

#assignment operators

num = 10
num = num + 10
print("number :", num)

nom =11
nom +=9
print("number:" , nom)

z = 10
z *= 5
print("number:",z)

x = 20
x /= 4
print("number:",x)

w = 50
w %= 8
print("number:", w)

v = 3
v **=4
print("number:",v)

#logical operators

#not
print(not False)
print(not True)
print(not (a>b))
print(not (a<b))

val1 = True
val2 = True
val3 = False

#and
print("and operator:", val1 and val2)
print("A:",(a==b) and (a>=b))
print("A:",(a==b) and (a<=b))

#or
print("or operator:",val1 or val3)
print("B:", (a==b) or (a>=b))
print("B:", (a==b) or (a<=b))

#type conversion 

# automatic conversion
t=int("3")
u=5.5
print(type(sum))
print(t + u)

r=float("3")
s=5.5
print(type(sum))
print(r + s)

s = str(s)

print(type(s))

#input

name = input("enter your name: ")
print("Welcome", name)

age = input("enter your age:")
print("Your age is:", age)

val = input("enter some value:")
print(type(val), val)

val = int(input("enter some value:"))
print(type(val),val)
val = float(input("enter some value:"))
print(type(val),val)

name = input("What is your name ?")
age = int(input("What is your age ?"))
marks = float(input("What are your Marks ?"))

print("Candidate name:",name)
print("Candidate age:",age)
print("Aquired marks:",marks)

#Practice problems

#Write a program to input 2 numbers and print thier sum
Number1 = int(input("Enter first number:"))
Number2 = int(input("Enter second number:"))
print("The sum of both numbers entered is", Number1 + Number2)

#Write a program to input side of a square and print its area
side = int(input("Enter side of square in cm:"))
side **= 2
print("Area of the square is",side,"cm.")

#Write a program to input 2 floating point numbers and print thier average

l = float(input("enter number 1:"))
m= float(input("enter number 2:"))
n = l + m
o = n/2
print("Average of the two numbers is:",o)

#Write a program to input 2 integer numbers and check if the statement obe is greater than another is true or false
h = int(input("first:"))
i = int(input("second:"))
print(h>i)

