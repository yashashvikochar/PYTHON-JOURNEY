# FUNCTIONS & RECURSION
print("Functions & Recursion")

# def 
# def is used to define a function in Python. 
# A function is a block of code that performs a specific task and can be reused multiple times throughout a program.

# Example of a simple function that calculates the area of a rectangle:
def calculate_area(length, width):
    area = length * width
    print("Area of rectangle is:", area) # prints the calculated area
    return area # returns the calculated area to the caller 

# Calling the function with arguments 24 and 5
calculate_area(24,5) 

def calculate_speed(d,t):
    speed = d/t
    print("Speed is:", speed,"m/s") 
    return speed

calculate_speed (120,50)

def flight_schedule(airline, departure, departure_time, arrival, arrival_time):
    print("Flight Schedule:")
    print("Airline:", airline)
    print("Departure:", departure,",",departure_time)
    print("Arrival:", arrival,",",arrival_time)
    return airline, departure, departure_time, arrival, arrival_time

flight_schedule("Boeing 234", "Mumbai", "10:00 AM", "New York", "2:00 PM")

# Practice problem
# Calculate average of marks of students for pcm using a function
def calculate_average(physics, chemistry, mathematics):
    average = (physics + chemistry + mathematics)/3
    print("Average marks of students in PCM is:", average)
    return average
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))
mathematics = int(input("Enter marks in Mathematics: "))
calculate_average(physics, chemistry, mathematics)

# "end" function
print("My name is:", end=" ")
print("Yashashvi Kochar")
# end=" " is used to specify what to print at the end of the output. 
# By default, it is a newline character, but you can change it to any string you want. 
# In this case, it is set to a space, so the next print statement will continue on the same line.
print("My name is", end=":")
print("Yashashvi Kochar")
# here, end=":" is used to specify that a colon should be printed at the end of the output instead of a newline character.

#default and non-default arguments
# In Python, you can define functions with default and non-default arguments.
# Non default is always written first and default is written after non-default arguments.
def engineering_branches(branch, degree="Engineering"):
    print(branch, degree)
    return branch, degree   
engineering_branches("Aerospace")
engineering_branches("Electronics and Communication")
engineering_branches("Electrical","Engineer")
# here, branch is a non-default argument and degree is a default argument. 
# If the user does not provide a value for degree, it will take the default value "Engineering".

# printing a list of branches using a function
branches = ["Aerospace", "Electronics and Communication", "Electrical", "Mechanical","Automobile","Computer Science","Information and Communication Technology", "Instrumentation And Control"]
def list_of_branches(branches):
    for branch in branches:
        print(branch, end=", ")

print("List of branches in Engineering:")   
list_of_branches(branches)
print()

# Write a function to find the factorial of a number using recursion.

#using loops
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1,n+1):
    factorial*=i
print(factorial)

# using function
n = int(input("Enter number:"))
def calculate_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)

calculate_factorial(n)

# Write a function to convert USD to INR
usd = int(input("Enter USD value:"))
def conversion_usd_to_inr(usd):
    inr = usd*96.29
    print(usd, "USD =", inr, "INR")
    
conversion_usd_to_inr(usd)

# RECURSION
# When a function calls itself repeatedly.

#recursive function 

# funtion to print values backward from 5
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(7)

# function to print factorial
def factorial_recursive(x):
    if x == 0 or x == 1:
        return 1
    return factorial_recursive(x - 1) * x

print(factorial_recursive(6))

# function to print sum of first k natural numbers

def sum_of_numbers(k):
    if(k==0):
        return 0
    return sum_of_numbers(k-1) + k

sum_of_first_k_natural_numbers = sum_of_numbers(5)
print(sum_of_first_k_natural_numbers)

# Function to print all elements in a list usinf index and list and recursion

def print_list(elements, idx):
    if (idx == len(elements)):
        return
    print(elements[idx])
    print_list(elements, idx+1)

cities_with_international_airports_in_India = ["Delhi","Mumbai","Chennai","Hyderabad","Kolkata","Bangalore","Ahmedabad"]
print_list(cities_with_international_airports_in_India, 0)  

