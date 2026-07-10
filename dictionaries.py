# Dictionaries store data in KEY : VALUE pairs
# written using curley brackets {}

student ={
    "name" : "Adam",
    "age" : 38,
    "major" : "FSDI"
}

print(student)

# Accessing item
print(student["name"]) # accessing by Key
print(student.get("age"))

# Adding new items
student["graduation_year"] = 2025
print(student)

# CHANGING Values
student["age"] = 39
print(student)

# REMOVING Items
student.pop("major") # Removes key "major" and its value
print(student)

# CHECKING if Key exists
if "name" in student:
    print("key 'name' exists")

# NESTED dictionaries
students = {
    "student1": {"name": "adam", "age":30},
    "student2": {"name": "Billy", "age":31}
}
print(students["student2"]["name"]) # Access nested value

print("------------------------------------")
# LOOPING through a dictionary
# .key()    -> just the keys
# .values() -> just the values
# .items()  -> key/values pair together

for key in student.keys():
    print(key)

for values in student.values():
    print(values)

for key, value in student.items():
    print(f"{key} : {value}")

# UPDATING MULTIPLE keys at once
# update() merges a second dictionary into the first one.
# Existing keys get overwritten, new keys get added
student.update({"age": 40, "gpa": 3.8})
print(student)

# TIP: highlight code and SHIFT to then wrap it in any bracket you need (), {} ect


"""
-------------------------------
MINI CHALLENGE: STUDENT REPORT CARD 
-------------------------------
You need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    -"subject"
    -"grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
    If between 70 and 89 → print "Good job!"
    Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""

print("---------------------------------------------")
report_card ={
    "name" : "adam",
    "subject" : "English",
    "grades" : (90, 60, 76)
}
print("Student", report_card["name"])
print("Student", report_card["subject"])


avg = sum(report_card["grades"]) / len(report_card["grades"])

report_card["average"] = avg
if avg >= 90:
    print("excellent")
elif avg >= 70:
    print("Good job")
else:
    print("needs improvemnet")

report_card.pop("subject")

print("updated report card: ", report_card)







# Solution
#
#
#
#
#
#
#
#










