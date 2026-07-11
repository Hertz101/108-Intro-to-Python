"""
A while loop repeats a block of code as a language as long as a condition is True.
be careful - if the condition never becomes False, you'll get an INFINITE loop!

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is:", count)   # infinite loop since it never counts to 5
    count += 1  # adds a count of 1 everytime it loops

print("----------------------------------------------")

# using BREAK to STOP the loop

number = 0

while True: # infinite loop
    print(number)
    number += 1
    if number == 3:
        break       # stops the loop when it reaches 3

print("----------------------------------------------")

# using CONTINUE to SKIP iteration
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue      #. skips 3
    print(count)

print("----------------------------------------------")

# ELSE with while

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")

print("----------------------------------------------")

"""
Mini Challenge: Password Checker 
1. Ask the user to enter a password
2. Check if it's correct (password: "secret123")
3. If it's wrong, print "Wrong! Try again." and ask again
4. When they enter the correct password, print "Access granted!"
"""

while True:
    password = input("Enter a password: ")      # asked the user to input their password and stored the variable
    if password == "secret123":                 # Checked if password is secret123 if so....
        print("Access granted!")                # GTG
        break                                   # Loop stops here
    else:                                       # If not correct
        print("Wrong! Try again.")              # this error pops up and loop returns to Enter Password:

print("----------------------------------------------")

password = ""

while password != "secret123":
    password = input("Enter password")
    if password != "secret123":
        print("wrong try again")

print("Access granted")