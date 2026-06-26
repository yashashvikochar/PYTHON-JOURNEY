# 03 LISTS AND TUPLES

#LISTS

print("03 LISTS AND TUPLES")

marks1 = 93.8
marks2 = 87.4
marks3 = 89.0
marks4 = 76.2
marks5 = 98.6

marks = [93.8,87.4,89.0,76.2,98.6]

print(marks)
print(type(marks))
print(marks[2])
print(len(marks))

# lists are mutable, strings are not

student = ["Yashashvi", 97, 18, "Ahmedabad"]
print(student[0])
student1 = ["Yashvi", 94, 17, "Mumbai"]
student1[0] = "Devika"
print(student1)

# List slicing

print(marks[:4])
print(marks[1:3])
print(marks[-4:-1])

# List Methods

# append: adds element at last
series = [4,5,8,2]
series.append(7) #adding print before this here returns nothing
print(series)

#sort: 
series.sort()    #adding sort before this here returns nothing
print(series)

series.sort(reverse=True)
print(series)

fruits = ["mango","apple","pineapple","banana"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#reverse: reverses only order
alphabets = ["a", "s","d","f","g"]
alphabets.reverse()
print(alphabets)

#insert
#(idx,el)
number = [5,6,8,9,3,0]
number.insert(4,7)
print(number)

#remove
#removes elemest from its first occurence
num = [2,3,6,0,5,3,7,6]
num.remove(3)
print(num)
num.remove(6)
print(num)

#pop
#removes from index
sequence = [5,9,3,7,3,2,]
sequence.pop(4)
print(sequence)

#TUPLES
#similar to list but cannot be changed
#() in place of []
  
tup = (3,6,2,8)
print(tup[1])
print(tup[3])

#empty  tuple
a = ()
print(tup)
print(type(tup))

#always put a comma in single element after or else value is considerd as integer
#if multiple coma isn't required after last one
b = (2,)
print(b)
print(type(b))

c = (3) 
print(c)
print(type(c))

#slicing
d = (2,4,7,9,0,4)
print(d[2:5])

#index
#finds index of element we want
e = (5,2,7,8)
print(e.index(2))

#count
# gives number of times element is there 
f = (4,7,8,4,3,5,4,0,11,4,6,4)
print(f.count(4))

#Practice Questions

#1 ask user to enter names of their 3 favourite movies and store them in a list

Movie1 = input("enter movie1:")
Movie2 = input("enter movie2:")
Movie3 = input("enter movie3:")

Movies = [Movie1, Movie2, Movie3]

print("List of your favourite movies is: ", Movies)


