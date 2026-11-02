# any thing that is enclosed in double quotes or single quotes is called string.

"Snehil" # length = 6 , counting starts from 0 to 5
#  string functions
name = "Snehil"
# (len)
print(len(name))  # Output: 6
print(name[0])   # Output: S
print(name[1:4]) # Output: neh

# string.endswith()  # checks if the string ends with the specified value
print(name.endswith("il"))  # Output: True

#  string.startswith()  # checks if the string starts with the specified value
print(name.startswith("Sn"))  # Output: True

# string.capitalize()  # converts the first character to upper case
print(name.capitalize())  # Output: Snehil

# string.find(word)  # searches the string for a specified value and returns the position of where it was found
print(name.find("eh"))  # Output: 2

# string.replace(old, new)  # replaces a specified value with another specified value
print(name.replace("Snehil", "John"))  # Output: John
