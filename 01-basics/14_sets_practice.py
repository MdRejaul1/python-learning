
# Python Sets Practice

# Problem 1: Create a Set
fruits = {"apple", "banana", "mango"}
print(fruits)


# Problem 2: Remove Duplicate Items
numbers = {1, 2, 2, 3, 3, 4, 4}
print(numbers)


# Problem 3: Create a Set Using set()
fruits = set(("apple", "banana", "mango"))
print(fruits)


# Problem 4: Access Set Items Using a Loop
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)


# Problem 5: Check if an Item Exists
fruits = {"apple", "banana", "mango"}
print("banana" in fruits)
print("grape" not in fruits)


# Problem 6: Add One Item
fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)


# Problem 7: Add Items from Another Iterable Using update()
fruits = {"apple", "banana"}
more_fruits = ["mango", "orange"]
fruits.update(more_fruits)
print(fruits)


# Problem 8: Add Items from Another Set
a = {"apple", "banana"}
b = {"mango", "orange"}
a.update(b)
print(a)


# Problem 9: Remove an Item Using remove()
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)


# Problem 10: Remove an Item Using discard()
fruits = {"apple", "banana", "mango"}
fruits.discard("grape")
print(fruits)


# Problem 11: Remove an Item Using pop()
fruits = {"apple", "banana", "mango"}
removed_item = fruits.pop()
print("Removed:", removed_item)
print("Remaining:", fruits)


# Problem 12: Empty a Set Using clear()
fruits = {"apple", "banana", "mango"}
fruits.clear()
print(fruits)


# Problem 13: Delete a Set Using del
fruits = {"apple", "banana", "mango"}
del fruits
# print(fruits)  # Uncomment to see the NameError


# Problem 14: Join Sets Using union()
a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print(result)


# Problem 15: Join Sets Using the | Operator
a = {"apple", "banana"}
b = {"banana", "mango"}
print(a | b)


# Problem 16: Join Multiple Sets Using union()
a = {1, 2}
b = {2, 3}
c = {3, 4}
print(a.union(b, c))


# Problem 17: Update a Set Using update()
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print(a)


# Problem 18: Find Common Items Using intersection()
a = {"apple", "banana", "mango"}
b = {"banana", "mango", "orange"}
result = a.intersection(b)
print(result)


# Problem 19: Find Common Items Using & Operator
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)


# Problem 20: Update Original Set Using intersection_update()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)


# Problem 21: Find Differences Using difference()
a = {"apple", "banana", "mango"}
b = {"banana", "orange"}
print(a.difference(b))
print(b.difference(a))


# Problem 22: Find Difference Using - Operator
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a - b)


# Problem 23: Update Original Set Using difference_update()
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print(a)


# Problem 24: Find Symmetric Difference
a = {"apple", "banana", "mango"}
b = {"banana", "orange", "grape"}
print(a.symmetric_difference(b))


# Problem 25: Symmetric Difference Using ^ Operator
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)


# Problem 26: Update Using symmetric_difference_update()
a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)


# Problem 27: Check if One Set Is a Subset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))


# Problem 28: Check if One Set Is a Superset
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))


# Problem 29: Check if Sets Are Disjoint
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))


# Problem 30: Copy a Set
original = {"apple", "banana", "mango"}
copied = original.copy()
copied.add("orange")
print("Original:", original)
print("Copied:", copied)


# Problem 31: Find the Length of a Set
numbers = {10, 20, 30, 40}
print(len(numbers))


# Problem 32: Set with Different Data Types
data = {"Python", 25, True, 5.8}
print(data)


# Problem 33: Set Comprehension
squares = {x ** 2 for x in range(1, 6)}
print(squares)


# Problem 34: Set Comprehension with a Condition
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)


# Problem 35: Convert a List to a Set to Remove Duplicates
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# Problem 36: Convert a Set to a List
numbers = {10, 20, 30, 40}
numbers_list = list(numbers)
print(numbers_list)


# Problem 37: Mixed Set Challenge
students_python = {"Rahim", "Karim", "Sakib", "Nabil"}
students_java = {"Karim", "Nabil", "Hasan"}

print("All students:", students_python | students_java)
print("Both courses:", students_python & students_java)
print("Only Python:", students_python - students_java)
print("Only one course:", students_python ^ students_java)
print("Python students:", len(students_python))
