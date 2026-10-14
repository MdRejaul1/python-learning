```python
# Python Lists Practice

# Problem 1: Access List Items
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[2])

# Problem 2: First and Last Items
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])

# Problem 3: Change List Items
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)

# Problem 4: Append Items
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

# Problem 5: Insert Items
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "orange")
print(fruits)

# Problem 6: Remove Items
fruits = ["apple", "banana", "mango", "orange"]
fruits.remove("banana")
print(fruits)

# Problem 7: Pop Items
fruits = ["apple", "banana", "mango", "orange"]
fruits.pop()
print(fruits)

# Problem 8: Length of a List
fruits = ["apple", "banana", "mango", "orange"]
print(len(fruits))

# Problem 9: Membership
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)

# Problem 10: Access Multiple Items
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[-1])
print(fruits[2])

# Problem 11: Change List Items
fruits = ["apple", "banana", "mango"]
fruits[1] = "grape"
print(fruits)

# Problem 12: Add Multiple Items
languages = ["HTML", "CSS"]
languages.append("Python")
languages.insert(1, "JavaScript")
print(languages)

# Problem 13: Remove Multiple Items
fruits = ["apple", "banana", "mango", "orange"]
fruits.remove("banana")
fruits.pop()
print(fruits)

# Problem 14: List Slicing
numbers = [10, 20, 30, 40, 50]
first_three = numbers[:3]
print(first_three)
print(len(numbers))

# Problem 15: Membership Operators
languages = ["Python", "JavaScript", "C++"]
print("Python" in languages)
print("Java" not in languages)

# Problem 16: Sort Ascending
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

# Problem 17: Sort Descending
numbers = [40, 10, 30, 20]
numbers.sort(reverse=True)
print(numbers)

# Problem 18: Copy Lists
original = ["red", "green", "blue"]
copied = original.copy()
copied.append("yellow")
print("Original:", original)
print("Copy:", copied)

# Problem 19: Join Lists
a = ["Python", "Java"]
b = ["HTML", "CSS"]
combined = a + b
print(combined)

# Problem 20: Mixed Challenge
fruits = ["banana", "mango", "apple", "orange"]
fruits.remove("mango")
fruits.append("grape")
fruits.sort()
print(fruits)
print(len(fruits))

# Problem 21: Sort Numbers
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)
```
```python
# Python Lists - Missing Topics Practice


# Problem 22: Change a Range of Items
fruits = ["apple", "banana", "mango", "orange"]

fruits[1:3] = ["grape", "kiwi"]

print(fruits)


# Problem 23: Extend a List
fruits = ["apple", "banana"]
more_fruits = ["mango", "orange"]

fruits.extend(more_fruits)

print(fruits)


# Problem 24: Insert Items Using a Loop
numbers = [10, 20, 30]
new_numbers = [40, 50]

for number in new_numbers:
    numbers.append(number)

print(numbers)


# Problem 25: Remove Items Using del
fruits = ["apple", "banana", "mango", "orange"]

del fruits[1]

print(fruits)


# Problem 26: Clear a List
numbers = [10, 20, 30, 40]

numbers.clear()

print(numbers)


# Problem 27: Loop Through a List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Problem 28: Loop Through a List Using Index
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


# Problem 29: List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# Problem 30: List Comprehension with a Condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# Problem 31: Count List Items
fruits = ["apple", "banana", "apple", "mango", "apple"]

print(fruits.count("apple"))


# Problem 32: Find an Item's Index
fruits = ["apple", "banana", "mango", "orange"]

print(fruits.index("mango"))


# Problem 33: Reverse a List
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)


# Problem 34: Copy a List Using list()
original = ["red", "green", "blue"]

copied = list(original)
copied.append("yellow")

print("Original:", original)
print("Copy:", copied)


# Problem 35: Join Lists Using extend()
a = ["Python", "Java"]
b = ["HTML", "CSS"]

a.extend(b)

print(a)


# Problem 36: Create a List Using the list() Constructor
fruits = list(("apple", "banana", "mango"))

print(fruits)


# Problem 37: Mixed List Challenge
numbers = [5, 2, 8, 2, 10, 4, 2]

print("Original:", numbers)
print("Count of 2:", numbers.count(2))

numbers.remove(2)
numbers.extend([12, 14])
numbers.sort()

print("Updated:", numbers)
print("Length:", len(numbers))
```
