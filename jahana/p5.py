


names_inp = input("Enter a list of names separated by spaces: ")

names = names_inp.split()

# Join all names into one string
one_string = "".join(names)

# Count the occurrence of 'a'
count_a = one_string.lower().count('a')

print("Total occurrence of 'a':", count_a)
