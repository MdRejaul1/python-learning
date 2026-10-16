
# Python Dictionaries Practice
# Problems 1–45

# 01. Create a Dictionary
student = {
    "name": "Rejaul",
    "age": 31,
    "course": "Python"
}
print(student)


# 02. Access Items Using Keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car["brand"])
print(car["model"])


# 03. Access Items Using get()
print(car.get("year"))


# 04. Get All Keys
print(car.keys())


# 05. Get All Values
print(car.values())


# 06. Get All Key-Value Pairs
print(car.items())


# 07. Check If a Key Exists
if "model" in car:
    print("Model exists")


# 08. Check If a Key Does Not Exist
if "color" not in car:
    print("Color does not exist")


# 09. Change an Item
student["age"] = 32
print(student)


# 10. Update an Item Using update()
student.update({"course": "Software Engineering"})
print(student)


# 11. Add a New Item
student["city"] = "Dhaka"
print(student)


# 12. Add Multiple Items Using update()
student.update({
    "country": "Bangladesh",
    "language": "Python"
})
print(student)


# 13. Update an Existing Key
student.update({"city": "Chattogram"})
print(student)


# 14. Remove an Item Using pop()
student.pop("language")
print(student)


# 15. Remove the Last Inserted Item
student.popitem()
print(student)


# 16. Delete an Item Using del
del student["age"]
print(student)


# 17. Delete the Entire Dictionary
temp = {"a": 1, "b": 2}
del temp
# print(temp)  # NameError


# 18. Empty a Dictionary Using clear()
data = {"name": "Ali", "age": 25}
data.clear()
print(data)


# 19. Loop Through Keys
person = {
    "name": "Ali",
    "age": 25,
    "city": "Dhaka"
}

for key in person:
    print(key)


# 20. Loop Through Values
for value in person.values():
    print(value)


# 21. Loop Through Key-Value Pairs
for key, value in person.items():
    print(key, value)


# 22. Print Key and Value With Formatting
for key, value in person.items():
    print(key + ":", value)


# 23. Access Values Using Keys in a Loop
for key in person:
    print(person[key])


# 24. Loop Through a Nested Dictionary
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}

for x, obj in myfamily.items():
    print(x)

    for y, value in obj.items():
        print(y + ":", value)


# 25. Copy Using copy()
original = {"a": 1, "b": 2}
copied = original.copy()
copied["c"] = 3

print(original)
print(copied)


# 26. Copy Using dict()
another_copy = dict(original)
print(another_copy)


# 27. Get the Number of Items
print(len(original))


# 28. Create a Dictionary Using dict()
user = dict(name="Rejaul", age=31)
print(user)


# 29. Create a Dictionary Using fromkeys()
keys = ("name", "age", "city")
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)


# 30. Use setdefault()
person = {"name": "Ali", "age": 25}

person.setdefault("city", "Dhaka")
print(person)

person.setdefault("name", "Karim")
print(person)


# 31. Dictionary Comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares)


# 32. Dictionary Comprehension With a Condition
even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}
print(even_squares)


# 33. Create a Dictionary From Two Lists
keys = ["name", "age", "city"]
values = ["Rejaul", 31, "Dhaka"]

result = dict(zip(keys, values))
print(result)


# 34. Filter Items From a Dictionary
marks = {
    "English": 85,
    "Math": 45,
    "Python": 92,
    "Science": 38
}

passed = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 50
}
print(passed)


# 35. Calculate Total Marks
marks = {
    "English": 85,
    "Math": 90,
    "Python": 95
}

total = sum(marks.values())
print("Total:", total)


# 36. Find the Highest Mark
highest = max(marks.values())
print("Highest mark:", highest)


# 37. Find the Subject With the Highest Mark
top_subject = max(marks, key=marks.get)
print("Top subject:", top_subject)
print("Highest mark:", marks[top_subject])


# 38. Count How Many Students Passed
results = {
    "Ali": 75,
    "Rafi": 42,
    "Karim": 65,
    "Hasan": 35,
    "Sami": 80
}

passed_count = 0

for mark in results.values():
    if mark >= 50:
        passed_count += 1

print("Passed:", passed_count)


# 39. Count the Frequency of Each Character
text = "banana"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)


# 40. Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)


# 41. Find Common Keys
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common_keys = dict1.keys() & dict2.keys()
print(common_keys)


# 42. Safely Access a Missing Key
person = {"name": "Ali", "age": 25}

print(person.get("city", "Not available"))


# 43. Update Values in a Dictionary
prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

for fruit in prices:
    prices[fruit] += 10

print(prices)


# 44. Build a New Dictionary From Existing Data
products = {
    "laptop": 50000,
    "mouse": 800,
    "keyboard": 1500,
    "monitor": 12000
}

expensive_products = {}

for product, price in products.items():
    if price >= 5000:
        expensive_products[product] = price

print(expensive_products)


# 45. Nested Dictionary Challenge
employees = {
    "emp1": {"name": "Rahim", "salary": 30000},
    "emp2": {"name": "Karim", "salary": 40000},
    "emp3": {"name": "Hasan", "salary": 35000}
}

total_salary = 0

for employee in employees.values():
    print(employee["name"], employee["salary"])
    total_salary += employee["salary"]

print("Total salary:", total_salary)
