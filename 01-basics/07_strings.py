# Python Strings

# Creating a string
name = "Arnob"

print(name)

# Strings can use single or double quotes
first_name = 'Arnob'
last_name = "Fardin"

print(first_name)
print(last_name)

# String with a variable
age = 21
message = "My name is Arnob and I am 21"

print(message)

# Multiline string
text = """Python is easy to learn.
Python is powerful.
Python is popular."""

print(text)

# Access a character using an index
word = "Python"

print(word[0])
print(word[1])

# Get the length of a string
print(len(word))

# Check if something is inside a string
print("Py" in word)

# Check if something is NOT inside a string
print("Java" not in word)

# Slicing
text = "Python"

print(text[0:3])
print(text[2:6])

# Modifying strings
message = "hello world"

print(message.upper())
print(message.lower())
print(message.replace("hello", "hi"))
print(message.strip())
# Escape characters

text = "He said \"Python is easy.\""

print(text)

# New line
print("Hello\nPython")

# Tab
print("Hello\tPython")

# Concatenating strings
first_name = "Arnob"
last_name = "Fardin"

full_name = first_name + " " + last_name

print(full_name)
# String Practice

# Problem 1
name = "  arnob fardin  "

name = name.strip().title()

print(name)


# Problem 2
username = "  MdRejaul1  "

username = username.strip().lower()

print(username)

