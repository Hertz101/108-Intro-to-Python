"""
A is-else statement in python is a conditional control structure that lets you decide which block of code to run depending on wether a condition is True or False

if condition:
    -Code block runs if condition is True
elif another_condition:  (else if)
    -Code block runs if first condition is False
    -and this condition is True
else:
    -Code block runs if none of the above conditions are True

if - checks a condition
elif - (else if) - checks another condition
else - runs if all other conditions are False    
"""



x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand IF statements
# you can write it all in one line

if x > 5: print("x is greater than 5")

# Short hand IF ... ELSE
print("Even") if x % 2 == 0 else print("odd")

x = 21
# Nested IF statements
if x > 0:
    if x < 20:
        print("x is a positive number less that 20")


# Combining conditions

age = 19

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")



"""
MINI CHALLENGE
1. Ask the user to enter their age and store it in a variable called age.
2. Ask the user if they have a valid ID
    (The user should enter "yes" or "no")
    Store the answer in a variable called has_id
3. Determine admission rules:
    - If age is 21 or older AND has_id is "yes":
        print "Access Granted!"
    - If age is 21 or older BUT has_id is "no":
        print " Access denied! - ID required"
    - If age is between 18 and 20 inclusive:
        print "Access Limited!"
    - Otherwise:
        print "access Denied - Too Young"
4. Create a variable called can_enter:
set it to Truw only if the user is 21 or older AND has_id is "yes"
otherwise set it to False

"""
user_age = input("Enter your age")
age = int(user_age)

if age <= 0:
    print("Invalid age entered")

valid_id = input("Do you have a valid ID?")
has_id = valid_id.lower() == "yes"

if age >= 21 and has_id:
    print("You're allowed to enter")
elif age >= 21 and not has_id:
    print("You're not allowed without ID")
elif age < 21 and age > 18 and has_id:
    print("You have limited access inside")
else:
    print("access denied")

can_enter = age >= 21 and has_id
if can_enter:
    print("you may enter the club")
else:
    print("see front desk")



