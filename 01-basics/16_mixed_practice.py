
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

# Problem 4: Book Inventory Checker

books = {
    "python": 5,
    "mindset": 0,
    "atomic habits": 3
}

print(books["python"])

if books["mindset"] == 0:
    print("Out of stock")
else:
    print("Available")
 # Problem 5: inventory stock status
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 3, 7]

for i in range(len(products)):
    if stock[i] == 0:
        print(products[i], "Out of Stock")
    elif stock[i] <= 5:
        print(products[i], "Low Stock")
    else:
        print(products[i], "In Stock")
