```python
# Python If...Else Practice


# Problem 1: Python If
age = 25

if age >= 18:
    print("You are an adult.")


# Problem 2: Python Elif
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")


# Problem 3: Python Else
temperature = 15

if temperature > 25:
    print("It is hot.")
else:
    print("It is not hot.")


# Problem 4: Short Hand If
x = 10
y = 20

if x < y: print("x is smaller than y")


# Problem 5: Short Hand If...Else
a = 15
b = 10

print("a is greater") if a > b else print("b is greater or equal")


# Problem 6: Python And
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")


# Problem 7: Python Or
day = "Saturday"

if day == "Friday" or day == "Saturday":
    print("It is a weekend.")


# Problem 8: Python Not
is_raining = False

if not is_raining:
    print("You can go outside.")


# Problem 9: Nested If
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID.")
else:
    print("You are too young.")


# Problem 10: Mixed If...Else Challenge
marks = 85
attendance = 90

if marks >= 80:
    if attendance >= 75:
        print("Passed with good marks.")
    else:
        print("Marks are good, but attendance is low.")
elif marks >= 40:
    print("Passed.")
else:
    print("Failed.")
```


