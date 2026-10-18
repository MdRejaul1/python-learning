
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
