```python
# Python Loops Practice
# For Loop and While Loop


# Problem 1: Print Numbers Using For Loop
for i in range(1, 6):
    print(i)


# Problem 2: Print Numbers Using While Loop
i = 1

while i <= 5:
    print(i)
    i += 1


# Problem 3: Print Even Numbers
for i in range(2, 11, 2):
    print(i)


# Problem 4: Sum of Numbers Using For Loop
total = 0

for i in range(1, 6):
    total += i

print("Total:", total)


# Problem 5: Sum of Numbers Using While Loop
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Total:", total)


# Problem 6: Loop Through a List
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)


# Problem 7: Print List Items Using While Loop
fruits = ["apple", "banana", "mango"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1


# Problem 8: Calculate List Total
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

print("Total:", total)


# Problem 9: Count Items Greater Than 10
numbers = [5, 12, 8, 20, 15, 3]
count = 0

for number in numbers:
    if number > 10:
        count += 1

print("Count:", count)


# Problem 10: Countdown Using While Loop
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Done!")


# Problem 11: Find a Number in a List
numbers = [4, 7, 10, 15, 20]
target = 15
found = False

for number in numbers:
    if number == target:
        found = True
        break

print("Found:", found)


# Problem 12: Skip a Number Using Continue
for i in range(1, 11):
    if i == 5:
        continue

    print(i)
```
