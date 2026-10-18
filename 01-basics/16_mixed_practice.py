
# Python Mixed Practice

# Problem 1: Bookstore Price Checker

bookstore = (250, 350, 400)

total = bookstore[0] + bookstore[1] + bookstore[2]

if total >= 800:
    print(True)
else:
    print(False)


# Problem 2: Book Search

books = ["python", "atomic habits", "mindset"]

store = books[0].capitalize()
print(store)

if "mindset" in books:
    print("Book found")
else:
    print("Book not found")

# Problem 3: Calculate Total Book Stock

books = {
    "python": 5,
    "mindset": 0,
    "atomic habits": 3
}

x = books.values()
total = 0

for item in x:
    total += item

print(total)
