person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
##LOOK AT THIS###value = dictionary [Key]**********%$#^@&&$&@
child = person["children"]
print(child[1])

print(person["children"][1])

#14 and 16 are the same, but prof prefers is we do it the second way over the first

# print out the name of the cat

dict_of_pets = person["pets"]
print(dict_of_pets["cat"])

print(person["pets"]["cat"])


# use a loop to print out the names of each child

#person["children"] is a list, but child is a string (because child goes through each element in the list)

for child in person["children"]:
    print(child)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet,name in person["pets"].items():
    print(f"The type of pet is: {pet} and the name of the pet is:{name}")