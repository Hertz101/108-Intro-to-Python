# Tuples are similar to lists
# But! Tuples are IMMUTALE (you cannot change them after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#ACCESSING ITEM
print(my_tuple[0])
print(my_tuple[1])

# Length of a tuple
print(len(my_tuple))

# NESTED TUPLES
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)

combine = (tuple1,tuple2)
print(combine)
print(tuple1,tuple2)

# SINGLE item tuples
# you must add a comma at the end or python won't recognize it as a tuple
single = ("water",)
print(type(single)) # this is a tuple
not_tuple = ("air")
print(type(not_tuple))

# COUNT and INDEX

letter = ("a", "b", "a", "c", "a")
print(letter.count("a")) # How many times "a" appears ->3
print(letter.index("c")) # The index where "c" first appears ->3 0,1,2,*3

# Tuple Unpacking
# You can "unpack" a tuple items directly into seperate variables

coordinates = (10, 20)
x, y = coordinates
print(x) # follows the parameters for the tuple
print(y) # x=10, y=20

person = ("Leo", 23, "Teacher")
name, age, job = person
print(f"My name is {name} and I am {age}, my job is {job}")


"""
-------------------------------
MINI CHALLENGE: CLASS QUIZ ANALYZER
-------------------------------
You are analyzing quiz scores stored in a tuple.
1. Create a tuple called "quiz_scores" with at least 6 integer scores.
2. Print the FIRST 3 scores and the LAST 3 scores using slicing.
3. Print the HIGHEST and LOWEST score using built-in functions.
4. Check if ANY score is below 70:
    If yes, print "Warning: At least one failing score!"
    Otherwise print "All students passed!"
5. Create a new tuple called "bonus_scores" where each score is increased by 5.
6. Combine "quiz_scores" and "bonus_scores" into a tuple called "final_scores".
7. Print the total number of scores in "final_scores".
8. Print the LAST score in "final_scores".
"""


#solution
quiz_scores = (85,92,72,78,55,67)
print(("First 3 scores:", quiz_scores[:3]))
print(("Last 3 scores:", quiz_scores[-3:]))

high_score = max(quiz_scores)
low_score = min(quiz_scores)
print(f"Highest Score: {high_score}")
print(f"Lowest Score: {low_score}")

if any(score < 70 for score in quiz_scores):
    print("Warning: At least one failing score")
else:
    print("All students passed")

bonus_scores = tuple(score + 5 for score in quiz_scores)

final_scores = quiz_scores + bonus_scores

print("total scores:", len(final_scores))

print("last score:", final_scores[-1])


