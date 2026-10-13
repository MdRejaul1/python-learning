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
```python
# Python If...Else - Mixed Practice
# Problems 11-25


# Problem 11: Positive, Negative, or Zero
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Problem 12: Even or Odd
number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 13: Find the Largest of Two Numbers
a = 25
b = 40

if a > b:
    print(a)
else:
    print(b)


# Problem 14: Find the Largest of Three Numbers
a = 15
b = 30
c = 20

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Problem 15: Voting Eligibility
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Problem 16: Grade Calculator
marks = 82

if marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")


# Problem 17: Login Check
username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")


# Problem 18: Weekend Checker
day = "Sunday"

if day == "Friday" or day == "Saturday":
    print("Weekend")
else:
    print("Working day")


# Problem 19: Temperature Checker
temperature = 32

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")


# Problem 20: Number Range
number = 45

if number >= 1 and number <= 100:
    print("Within range")
else:
    print("Outside range")


# Problem 21: Short Hand If
balance = 500

if balance > 0: print("Positive balance")


# Problem 22: Short Hand If...Else
number = 8

print("Even") if number % 2 == 0 else print("Odd")


# Problem 23: Not Operator
is_raining = False

if not is_raining:
    print("Go outside")
else:
    print("Stay inside")


# Problem 24: Nested If - Membership
age = 22
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed")
    else:
        print("Ticket required")
else:
    print("Age requirement not met")


# Problem 25: Mixed Challenge
age = 24
has_id = True
has_ticket = False

if age >= 18 and has_id:
    if has_ticket:
        print("Entry allowed")
    else:
        print("Buy a ticket")
else:
    print("Entry denied")

