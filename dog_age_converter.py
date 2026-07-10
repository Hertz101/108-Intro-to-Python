# Used a basic print() to create the title below in the terminal.
print("-----------Dog Age Converter------------")
print("")
# Created an input function with int(Integer) then prompt the user to input the age of their dog.
dog_age = int(input("Enter your dog's age in human years:"))

# Converted the input from the input function above (human years) then multiplied by 7 then converted to an int
dog_years = dog_age * 7

"""Created an f String telling the user how old thier dog is by adding the results (age) from
    the input (dog_age x 7 = age) followed by the rest of the print "years old in dog years" """

print(f"Your dog is {dog_years} years old in dog years!")
print("")
