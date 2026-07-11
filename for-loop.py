"""
A for loop in python is a control structure that lets you repeat a  block of code in a sequence (list, string, tuple, set, or any range of numbers)

it is used when you know how many times you want to repeat an action or process each element in a collection

for variable in sequence:
    #Code block runs for each item in a sequence
"""
# loop through a List
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)

print("--------------------------------------")

# Loop through a string
for letter in "Hello":
    print(letter)

print("--------------------------------------")

# range() generates a sequence of numbers

for x in range(5):  #3 STOPS AT INDEX 5
    print(x)        # prints 0-4

print("--------------------------------------")

# start and stop range()
for x in range(2, 6):   # stops at index 5
    print(x)            # prints 2-5

print("--------------------------------------")

# start, stop, step
for number in range(0, 10, 2):  # stops at index 8 skipping every other number from 0
    print(number)               # prints 2-8 by two's

print("--------------------------------------")

# ELSE in for loop
for x in range(3):
    print(x)
else: # run when the loop is done
    print("Loop is finished") # you can add a comment like finished

print("--------------------------------------")

# Break and CONTINUE in for loops
for x in range(10):
    if x == 5:      # if- condition check
        continue    # Skip 5 to continue to next iteration
    if x == 8:      # 8 index = 7
        break       # STOP loop completely
    print(x)

print("--------------------------------------")

# ENUMERATE () get the index AND the value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)     # o apple, 1 banana, 2 cherry

print("--------------------------------------")

# You can even choose where the counting starts
for index, fruit in enumerate(fruits, start=4):
    print(f"{index}. {fruit}")

print("--------------------------------------")

# ZIP() loop through two lists together

names = ["Leo", "Alex", "Nina"]
scores = [92, 85, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

print("--------------------------------------")

# NESTED for loops

for row in range(1, 4):
    for col in range(1,4):
        print(f"({row}, {col})", end = "")
    print() # move to a new line afrer each row finishes  

print("--------------------------------------")

"""
MINI CHALLENGE
1. Ask the user to enter a number and store it in a variable called num.
2. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10)
3. Inside the loop, multiply num by the current loop value (1)
"""

num = int(input("Enter any number: "))

for x in range(1, 11):
    
    result = num * x
    print(f"{num} x {x} = {result}")

print("--------------------------------------")


num - int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")



