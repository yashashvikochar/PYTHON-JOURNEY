#DICTIONARY AND SET IN PYTHON
print("DICTIONARY AND SET IN PYTHON")

##### DICTIONARY
# Dictionary is a collection of key-value pairs. 
# Each key is unique, and it is used to access the corresponding value. 
# Dictionaries are mutable, meaning you can change their content without changing their identity.
# Dictionaries are unordered
# Dictionaries are defined using curly braces {} and key-value pairs are separated by colons (:).
# Dictionaries don't allow duplicate keys, but they can have duplicate values.



INFO = {
    "Name": "Yashashvi",
    "Age": 18,
    "City": "Ahmedabad",
    "Is_Student": True,
    "Last_Class_Attended": "Class 12",
    "Subjects_studied": ("Physics", "Chemistry", "Math", "English", "Physical Education"),
    "Languages_known": ("English", "Hindi", "Gujarati", "Marathi", "Marwari")
}
print(INFO)

#Changing the value of a key
INFO["name"] = "Yashashvi Kochar"
print(INFO)

# Adding a new key-value pair
INFO["school"] = "Ahmedabad Public School International" 
print(INFO)

# key can be any value type, but it must be immutable (like strings, numbers, or tuples).

# Real-world avionics system dictionary example
cockpit_telemetry = {
    "flight_number": "AI-101",
    "current_altitude": 35000,
    "airspeed_knots": 460,
    "fuel_level_percent": 84.5
}
print(cockpit_telemetry["current_altitude"])

#Null Dictionary
null_dict = {}
null_dict["College"] = "Yet to be decided"
print(null_dict)

#Nested Dictionary
nested_dict = {
    "Flight" : "A-01",
    "Telemetry" : {
        "Altitude" : 35000,
        "Airspeed" : 460,
        "Fuel_Level" : 84.5
    },
}
print(nested_dict["Telemetry"])
print(nested_dict["Telemetry"]["Fuel_Level"])

# Dictionary Methods

# dict.keys() - Returns a list of all keys in the dictionary

print(INFO.keys())
print(nested_dict.keys())

#  How to convert the keys to a list
keys_list = list(INFO.keys())

print(keys_list)

#Total number of keys in the dictionary len(dict.keys())

print(len(INFO.keys()))

# Length of list of keys in nested dictionary

print(len(list(nested_dict["Telemetry"].keys())))

# dict.values() - Returns a list of all values in the dictionary

print(INFO.values())
print(list(INFO.values()))

print(list(nested_dict.values()))

# dict.items() - Returns a list of key-value pairs as tuples

print(INFO.items())
print(list(INFO.items()))
print(list(nested_dict.items()))

# dict.get(key) - Returns the value for the specified key, or None if the key is not found

print(INFO.get("City"))
print(INFO.get("Country"))  # Returns None since "Country" key is not present
# print(INFO["Country"])  # Raises KeyError since "Country" key is not present
print(INFO["Name"]) # Returns the value for the "Name" key

print(nested_dict.get("Telemetry").get("Airspeed")) # Returns the value for the "Airspeed" key in the nested dictionary

# dict.update(other_dict) - Updates the dictionary with key-value pairs from another dictionary

nested_dict.update({"Reach Time": "India Time 12:30 PM"})
print(nested_dict)

# dict.pop(key) - Removes the key-value pair with the specified key and returns the value


# dict.popitem() - Removes and returns an arbitrary key-value pair as a tuple


# dict.clear() - Removes all key-value pairs from the dictionary


# dict.copy() - Returns a shallow copy of the dictionary


##### SETS

# A set is an unordered collection of unique elements. Output is not as we have given in the input. It is unordered and does not maintain any specific order of elements.   

# Sets are mutable, meaning you can add or remove elements from a set after it is created.
# Elements in a set are immutable.
# Sets are defined using curly braces {} or the set() constructor.
# Sets do not allow duplicate elements, and they do not maintain any specific order of elements.
# Sets are commonly used for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference.         
# Sets are useful when you want to store a collection of items and ensure that each item is unique.
# Sets are often used in scenarios where you need to perform operations like finding common elements between two collections or removing duplicates from a list.    

Series = {10, 19, 36, 25, 19, 10, 93}
print(Series)
print(len(Series))  # Output: 5 (duplicates are removed)

# Empty Set
empty_set = set() # write *set()*
print(empty_set)

# Methods of Set

# ADDING ELEMENTS TO SET
# set.add(element) - Adds an element to the set

# Radar pings Sector A multiple times (Notice the duplicate flight numbers)
radar_pings_sector_A = set()
radar_pings_sector_A.add("AI101")
radar_pings_sector_A.add("6E203")
radar_pings_sector_A.add("UK501")
radar_pings_sector_A.add("AI101")  # Duplicate flight number
radar_pings_sector_A.add("6E203")  # Duplicate flight number
radar_pings_sector_A.add("UK401")  
radar_pings_sector_A.add("4W501")  

print("Unique aircraft currently in Sector A:")
print(radar_pings_sector_A)

print("Total unique aircraft in Sector A:", len(radar_pings_sector_A))

# REMOVING ELEMENTS FROM SET
# set.remove(element) - Removes an element from the set. Raises KeyError if the element is not found.

radar_pings_sector_A.remove("UK501")  # Removes the flight number "UK501" from the set
print("After removing UK501, unique aircraft currently in Sector A:")
print(radar_pings_sector_A) 

# POPPING ELEMENT FROM SET
# set.pop() - Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.

popped_flight = radar_pings_sector_A.pop()  # Removes and returns an arbitrary flight number from the set
print("Popped flight number:", popped_flight)
print("Popped flight number:", popped_flight)
print("Popped flight number:", popped_flight)

# EMPTYING A SET
# set.clear() - Removes all elements from the set

radar_pings_sector_A.clear()
print("After clearing the set:")
print(radar_pings_sector_A) 
print(len(radar_pings_sector_A))  # Output: 0 (set is now empty)

# UNION OF SETS
# set.union(other_set) - Returns a new set containing all unique elements from both sets
SectorA = {"A01", "A02", "A03", "A04"}
SectorB = {"B01", "B02", "B03", "B04"}
print("Unique aircraft in Sector A and Sector B:")
print(SectorA.union(SectorB))  # Output: {'A01', 'A02', 'A03', 'A04', 'B01', 'B02', 'B03', 'B04'}
print("Total unique aircraft in Sector A and Sector B:", len(SectorA.union(SectorB)))  # Output: 8

# INTERSECTION OF SETS
# set.intersection(other_set) - Returns a new set containing only the elements that are common to both sets
SectorC = {"A01", "B02", "B03", "A04"}
print("Unique aircraft in Sector A and Sector C:")
print(SectorA.intersection(SectorC)) # Output: {'A01', 'A04'} (common elements in both sets)
print("Total unique aircraft in Sector B and Sector C:")
print(SectorB.intersection(SectorC)) # Output: {'B02', 'B03'} (common elements in both sets)


#Practice Questions

#1 Store words and thier meanings in a dictionary and print the meaning of a word entered by user.

words = {
    "seed": "the part of a plant that can grow into a new plant",
    "sprout": "a young shoot or growth of a plant",
    "sapling": "a young tree that is still growing",
    "leaf": "a flat, green structure that grows on a plant",\
    "flower": ["the reproductive structure of a plant that produces seeds", "the most beutiful part of a plant"],
    "fruit": "the mature ovary of a flowering plant that contains seeds",
    "tree": "a plant with a trunk and branches",
    "river": "a natural watercourse",
    "mountain": "a large landform that rises above the surrounding land",
    "ocean": "a vast body of salt water that covers almost three-quarters of the Earth's surface",
    "sea": "a large body of salt water that is smaller than an ocean",
    "desert": "a barren area of land with little rainfall and sparse vegetation",
    "forest": "a large area covered chiefly with trees and undergrowth",
    "sky": "the expanse of air over the Earth, seen from the ground",
    "sun": "the star at the center of our solar system that provides light and heat",
    "moon": "the natural satellite of the Earth that orbits around it and reflects sunlight",
    "star": "a luminous point in the night sky that is a distant sun",
    "unierse": "all of space and everything in it, including stars, planets, galaxies, and other celestial objects"
    }

print("Words available in the dictionary are: ", list(words.keys()))
word = input("Enter the word to get its meaning: ")
if(word in words):
    print("Meaning of the word is: ", words[word])
else:
    print("Word not found in the dictionary.")

#2 You are given a list  of subject. If one classroom is required for each subject, then how many classrooms are required? 
S1= input("Enter subject 1: ")
S2= input("Enter subject 2: ")  
S3= input("Enter subject 3: ")
S4= input("Enter subject 4: ")
S5= input("Enter subject 5: ")
S6= input("Enter subject 6: ")
S7= input("Enter subject 7: ")
S8= input("Enter subject 8: ")
S9= input("Enter subject 9: ")
S10= input("Enter subject 10: ")
subjects = {
    S1, S2, S3, S4, S5, S6, S7, S8, S9, S10
}
print("List of subjects is: ", subjects)
print("Total number of classrooms required is: ", len(subjects))

#3 Write a program to to enter marks of 5 subjects and store them in a dictionary. Start with an empty dictionary and then add the marks of each student to the dictionary. Finally, print the dictionary containing the marks of all students.

marks_dict = {}

marks_dict_A = int(input("Enter A subject's marks"))
marks_dict.update({"A" : marks_dict_A})

marks_dict_B = int(input("Enter B subject's marks"))
marks_dict.update({"B" : marks_dict_B})

marks_dict_C = int(input("Enter C subject's marks"))
marks_dict.update({"C" : marks_dict_C})

marks_dict_D = int(input("Enter D subject's marks"))
marks_dict.update({"D" : marks_dict_D})

marks_dict_E = int(input("Enter E subject's marks"))
marks_dict.update({"E" : marks_dict_E})

print(marks_dict)

#4 Figure out a way to store 9 and 90 as seperate values in set (using built in data types )
values = {9,9.0} #gives only 9 
print(values)

values1 = {"9","9.0"} 
print(values1)    #gives seperate

values2={
    ("float", 9.0),
    ("int", 9)
}
print(values2)  #gives seperate