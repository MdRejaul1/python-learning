
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

# problem 6 : Online Store Discount Calculator

customers = ["Rahim", "Karim", "Sakib"]
amounts = [1200, 800, 2500]

for x in range(len(customers)):
    if amounts[x] >= 2000:
        discount = amounts[x] * 20 / 100
    elif amounts[x] >= 1000:
        discount = amounts[x] * 10 / 100
    else:
        discount = 0

    total = amounts[x] - discount

    print("Customer:", customers[x])
    print("Original Amount:", amounts[x])
    print("Discount:", discount)
    print("Final Amount:", total)
    print()
# problem 7 : product_inventory_discount
products = ["Book", "Pen", "Bag"]
prices = [500, 20, 1200]
stocks = [5, 0, 3]

total_price = 0

for x in range(len(products)):
    print(products[x], prices[x], stocks[x])

    if stocks[x] >= 1:
        if prices[x] >= 1000:
            discount = prices[x] * 15 / 100
        else:
            discount = prices[x] * 5 / 100

        print("Discount:", discount)

        Final_Price = prices[x] - discount
        print("Final Price:", Final_Price)

        total_price += Final_Price
    else:
        print("Out of Stock")

print("Total Price:", total_price)
