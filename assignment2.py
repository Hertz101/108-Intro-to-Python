print("List:")
# List
the_list = ["ford", "Chevy", "Dodge", "Toyota", "Tesla"]
print(the_list)


# Accessing items by index
print(the_list[0])
print(the_list[1])
print(the_list[2])
print(the_list[3])
print(the_list[4])

# Replacing values
the_list.append("Lexus")
print(the_list)

the_list.insert(4, "Ferrari")
print(the_list)

# Removing items by value 
the_list.remove("Tesla")
print(the_list)

# Removing items by index
the_list.pop(-1)
print(the_list)

# Print list length
print(len(the_list))
print(the_list)

print("--------------------------------------------")
print("Dictionary")

motorcycle = {
    "make"  :   "Harley Davidson",
    "year"  :   1949,
    "model" :   "panhead"
}
print(motorcycle)

# Accessing values using keys
print(motorcycle["model"])
print(motorcycle.get("year"))


# Adding new keys
motorcycle["next_model"] = 1950
print(motorcycle)

# Updating existing values
motorcycle["year"] = 1948
print(motorcycle)

# Removing keys
motorcycle.pop("make")
print(motorcycle)

print(motorcycle)