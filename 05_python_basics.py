# 05 LOOPS
# Loops are used to repeat a block of code multiple times. 
# In Python, there are two main types of loops: for loops and while loops.
# Loops are useful for iterating over sequences (like lists, tuples, and strings) or for executing a block of code as long as a certain condition is true.

# For Loops
# A for loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.

#while True:
#    print("This is an infinite loop. Press Ctrl+C to stop it.") infinite loop

height = 0
while height <= 1000:
    print("Takeoff height is:", height ,"metres")
    height += 50  # Increments the count by 50m

# Practice Problems

#1 Print numbers 1 to 200

initial_number = 1
while initial_number <= 200:
    print(initial_number)
    initial_number +=1

#2 Print numbers from 59 to -3

number = 59
while number >=-3:
    print(number)
    number -=1

#3 print multipliction table of any number n

count = 1
num = int(input("Enter number for mutiplication:"))
while count <= 10:
    print(num,"*", count,"=", num * count)
    count += 1

#4 Print square numbers of 1 to 20

i = 1
while i <= 20:
    print("Square of", i, "is :", i*i)
    i +=1

#5 Search if a number is a square of 1 to 10


squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a = int(input("enter number"))
i = 1
while i < len(squares):
    if(squares[i] == a):
        print("Found number at index:",i)
    else:
        print("Finding...")
    i += 1

# Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.

x = 1
while x <= 20 :
    print(x)
    if x == 16:
        break
    x += 1

# Continue Statement
# The continue statement is used to skip the rest of the code inside a loop for the current iteration and move on to the next iteration.

y = 1
while y <= 20:
    y += 1
    if y % 2 == 0:
        continue
    print(y)
# Skips even numbers and prints only odd numbers from 1 to 20

# For Loops
# A for loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.
# For loops are often used when the number of iterations is known beforehand.

list = [1, 2, 3, 4, 5]
for numbers in list:
    print(numbers)

Airports_in_India = ["DEL", "BOM", "BLR", "HYD"]
for airport in Airports_in_India:
    print(airport)
 
for airport in Airports_in_India:
    if airport == "BLR":
        print("Found BLR in the list.")
        break
    print(airport)

string = "Engineering Student"
for char in string:
    print(char)

for char in string:
    if char == "r":
        print("Found r in the string.")
        break
    print(char)
else:
    print("r not found in the string.")

# Practice Problems

#1 Print square numbers of 1 to 20 using for loop

square_number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for i in square_number:
    print("Square of", i, "is:", i*i)

#2 Search for a square number in the list of squares using for loop
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = int(input("Enter a number to search in the list of squares: "))
for square in squares:
    if square == a:
        print("Found number:", square)
        break

# Range Function

# The range() function is used to generate a sequence of numbers. It is often used in for loops to specify the number of iterations.
# The range() function can take one, two, or three arguments:
# range(stop): Generates numbers from 0 to stop-1
# range(start, stop): Generates numbers from start to stop-1
# range(start, stop, step): Generates numbers from start to stop-1, incrementing by step
# start defaults to 0, and step defaults to 1 if not specified.

for q in range(10): #range(stop) generates numbers from 0 to 9
    print(q)  

for q in range(5, 15): #range(start, stop) generates numbers from 5 to 14
    print(q)  

for q in range(2, 20, 3): #range(start, stop, step) generates numbers from 2 to 19, incrementing by 3
    print(q)  

# Practice Problems

#1 Print even numbers from 0 to 100
for q in range(101):
    if q % 2 == 0:
        print(q)  # Prints even numbers from 0 to 100

#2 Print numbers from 100 to 1 in reverse order
for q in range(100, 0, -1):
    print(q)  # Prints numbers from 100 to 1 in reverse order   

# Print multiplication table of a number t using range() function
t = int(input("Enter a number for multiplication table: "))
for q in range(1, 11):
    print(t, "*", q, "=", t * q)  # Prints multiplication table of t from 1 to 10

# Pass Statement
# The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in loops, functions, classes, or conditional statements where code is syntactically required but no action is needed.

for q in range(5):
    pass  # This loop does nothing and serves as a placeholder
# Can be used in situations where the code is not yet implemented or when a loop is required syntactically but no action is needed.
print("This is a placeholder loop that does nothing.")

# Practice Problems

# Write a program to find the sum of all even numbers from 1 to 100 using a for loop and the pass statement.
sum_even = 0
for q in range(1, 101):
    if q % 2 == 0:
        sum_even += q
    else:
        pass  # Do nothing for odd numbers
print("The sum of all even numbers from 1 to 100 is:", sum_even)

# Write a program to find faactorial of first 10 numbers using a for loop and the pass statement.
factorial = 1
for q in range(1, 11):
    factorial *= q
    pass  # Placeholder for any additional logic if needed
print("The factorial of the first 10 numbers is:", factorial)

