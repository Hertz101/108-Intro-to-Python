# SETS are UNORDERED, UNINDEXED, and have no DUPLICATES
# Created using {}

fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits)

# checking if item exists
print("apple" in fruits)

# Adding Items
fruits.add("orange")
print(fruits)

# ADDING MULTIPLE items
fruits.update(["kiwi", "water"])
print(fruits)

# REMOVING items
fruits.remove("banana")
print(fruits)

# if you're not sure item exists, use discard()to avoid errors
fruits.discard("water")
print(fruits)

# SET OPERATIONS (like in math)
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))         # combine both (no duplicates)
print(set1.intersection(set2))  # common elements (duplicates only)
print(set1.difference(set2))    # whats only in set 1
print(set1.symmetric_difference(set2))  #EVERYTHING except whats shared

# FROZENSET (a "locked" set)
locked_set = frozenset(["a", "b", "c"])
print(locked_set)
#locked_set.add("d")


"""
-------------------------------
MINI CHALLENGE: PARTY GUEST LIST
-------------------------------
You’re organizing a party! You have two sets of guests.
1. Create two sets:
    invited_friends = {"Alex", "Sam", "Leo", "Nina"}
    rsvped = {"Nina", "Sam", "Jordan"}
2. Print:
    Everyone who was invited (union)
    Everyone who said they’re coming (rsvped)
    Who hasn’t replied yet (difference)
3. Add two new names to invited_friends.
4. One of the people canceled — remove them from rsvped.
5. Print how many total confirmed guests are attending.
6.Check if "Leo" is still coming — print a message depending on the result.
"""

invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

print(invited_friends.union(rsvped))    #union
print(invited_friends.difference(rsvped))

invited_friends.update(["Chucky", "bobby"])
print(invited_friends)
rsvped.discard("Sam")
print(rsvped)


print("Total Confirmed", len(rsvped))
if "Leo" in rsvped:
    print("Yes")
else:
    print("No")