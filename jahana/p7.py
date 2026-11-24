string = input("Enter a string: ")

first_char = string[0]

string = string.replace(first_char, '$')

string = first_char + string[1:]

print("Result:", string)
