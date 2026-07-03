print("Hello world from python!")
print(2)
print(5 + 3)
print(True)

# SHORTCUTS
# command + s
# up arrow key
# #python3 then file
# command + - zoom out or in window

""" 
This is multi line comment
Tripple quotes around your comment
""" 

# Variables and concatenation
name = "Leo"
age = 24
print(name, age)

print("My name is " + name + " and I am " + str(age) + " years old")

"""
mini challenge 1
write a short story variables
1. Declare and initialize 5 varibles (strings and numbers)
2. Use print() and concatenation to tell a story
3. run in the terminal
"""

make = "Ford"
model = "bronco"
name = "Karl"
year = "1996"
state = "California"

print( "I saw " + name + " was driving his " + str( year ) , make , model ,"thru the redwoods in" , state )

# F String
print(f"I saw {name} was driving his {year},{make},{model} thru the redwoods {state}")

# multi line f string

print(f"""I saw {name} was driving 
        his {year} {make} {model} thru 
    the redwoods {state}""")

# Type Functions
print(type(name))
print(type(year))
print(type(True))

# Casting (chaneg data types)
print(20 + int("20"))
print(20 + age)

# INPUT FUNCTION
user_name = int(input("Enter your age: "))
print(f"Hello, {user_name}!")
# Always returns string
#print(type(input("Enter your age: ")))

# Converting input to int
new_age = int(input("Enter your age: "))
print(user_name + new_age)

"""
Pizza Calculator
1. ask how many slices of pizza and how many people
2. use math operators to calculate slices per person (divide /)
3. show the results with an f-string
"""

pizza_eaters = int(input("How many people want a slice of pizza?"))
pizza_sclices = int(input("How many slices do you wan't? "))
slice_per_person = pizza_eaters / pizza_sclices
print(f"This is how much you get {slice_per_person}")
