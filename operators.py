# arithmetic operators - used with numeric values to perform common
# math operations

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res = x ** y
print(res)

res = x // y
print(res)

# Assignment operators - used to assign values to variables
# =  means " put this values inide the (variables)"
# +=, -+, *=, /+ are shortcuts

x = 5.2345
x += 5
x -= 3
x *= 3
x /= 2
print(x)

# Comparison operators - used to compare two values
# == (eaqual to), !=(not equal to), <= (less than) >=(greater than)

# logical operators - used to combine conditional statements (booleans T/F)
# and -> both must be True
# or -> at least one must be true
# not-> flips True to False (vice versa)

x = 3
y = 10
z = 10

print(x == y and y == z)#False, because both conditions are not true
print(x == y or y == z) # true, because one condition is True
print(not x == y)       # True, because x != y

#Membership operator - used to test if a sequence is presented in an object
# in -> checks is something is inside a sequence (list, string, ect)
# not in -> checks if something is NOT in a sequence

x = [1, 2, 3, 4, 5]

print(4 in x)
print(9 not in x)

