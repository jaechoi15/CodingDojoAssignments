# The owner of a store wants a program to track products. Create a product class to fill the following requirements.
# Product Class:
# Attributes:
# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:
# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def addTax(self, tax):
        tax_amount = self.price * tax
        self.price = self.price + tax_amount
        return self
    
    def returnReason(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason == "in the box":
            self.status = "For Sale"
        elif reason == "opened":
            self.status = "Used"
            discount = self.price * .20
            self.price -= discount
        return self

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Item Name: " + self.item_name
        print "Weight: " + str(self.weight) + "lbs"
        print "Status: " + str(self.status)

print "*"*10 + "Product #1" + "*"*10
product1 = Product(1000, "Laptop", 4, "HP")
product1.sell().displayInfo()

print "*"*10 + "Product #2" + "*"*10
product2 = Product(700, "Phone", 1, "Samsung")
product2.returnReason("opened").displayInfo()

print "*"*10 + "Product #3" + "*"*10
product3 = Product(400, "TV", 20, "LG")
product3.returnReason("defective").displayInfo()

print "*"*10 + "Product #4" + "*"*10
product4 = Product(15, "Gloves", 1, "Head")
product4.returnReason("in the box").displayInfo()

print "*"*10 + "Product #5" + "*"*10
product5 = Product(400, "TV", 20, "LG")
product5.addTax(.06).returnReason("in the box").displayInfo()

print "*"*10 + "Product #6" + "*"*10
product6 = Product(300, "Snowboard", 20, "Burton")
product6.addTax(.06).sell().returnReason("opened").displayInfo()