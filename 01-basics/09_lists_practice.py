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
