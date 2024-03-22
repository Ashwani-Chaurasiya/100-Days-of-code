programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retriveing items form dictionary.
programming_dictionary["Bug"]

# Adding new items to dictionary
programming_dictionary['Loop'] = "The action of doing something over and over again."
print(programming_dictionary)

## wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

## edit an item in a dictionary
programming_dictionary["Bug"] = "A math in your computer"
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
