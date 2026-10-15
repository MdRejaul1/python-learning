```python
# Python Tuples Practice


# Problem 1: Create a Tuple
fruits = ("apple", "banana", "mango")

print(fruits)


# Problem 2: Access Tuple Items
fruits = ("apple", "banana", "mango", "orange")

print(fruits[0])
print(fruits[-1])


# Problem 3: Access a Range of Items
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])


# Problem 4: Check if an Item Exists
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("grape" not in fruits)


# Problem 5: Update a Tuple
fruits = ("apple", "banana", "mango")

temp = list(fruits)
temp[1] = "orange"
fruits = tuple(temp)

print(fruits)


# Problem 6: Add Items to a Tuple
fruits = ("apple", "banana")

temp = list(fruits)
temp.append("mango")
fruits = tuple(temp)

print(fruits)


# Problem 7: Remove Items from a Tuple
fruits = ("apple", "banana", "mango")

temp = list(fruits)
temp.remove("banana")
fruits = tuple(temp)

print(fruits)


# Problem 8: Unpack a Tuple
fruits = ("apple", "banana", "mango")

(first, second, third) = fruits

print(first)
print(second)
print(third)


# Problem 9: Unpacking with Asterisk
fruits = ("apple", "banana", "mango", "orange", "kiwi")

(first, *middle, last) = fruits

print(first)
print(middle)
print(last)


# Problem 10: Loop Through a Tuple
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)


# Problem 11: Loop Through Tuple Using Index
fruits = ("apple", "banana", "mango")

for i in range(len(fruits)):
    print(i, fruits[i])


# Problem 12: Join Two Tuples
a = ("Python", "Java")
b = ("HTML", "CSS")

combined = a + b

print(combined)


# Problem 13: Multiply a Tuple
numbers = (1, 2, 3)

repeated = numbers * 3

print(repeated)


# Problem 14: Count Items
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))


# Problem 15: Find an Item's Index
fruits = ("apple", "banana", "mango", "orange")

print(fruits.index("mango"))


# Problem 16: Find the Length
fruits = ("apple", "banana", "mango")

print(len(fruits))


# Problem 17: Create a Tuple with One Item
single_item = ("apple",)

print(single_item)
print(type(single_item))


# Problem 18: Create a Tuple Using tuple()
fruits = tuple(("apple", "banana", "mango"))

print(fruits)


# Problem 19: Tuple with Different Data Types
data = ("Arnob", 25, True, 5.8)

print(data)


# Problem 20: Mixed Tuple Challenge
numbers = (5, 2, 8, 2, 10, 4)

print("Original:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 8:", numbers.index(8))
print("Length:", len(numbers))

combined = numbers + (12, 14)

print("Combined:", combined)
```
