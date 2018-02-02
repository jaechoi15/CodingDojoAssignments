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

class Products(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        
    def sell(self):
        self.status = "Sold"
        return self
    
    def add_tax(self):
        tax = .065
        self.price += self.price * tax
        return self

    def item_return(self, reason):
        self.return_reason = reason
        if self.return_reason == "Defective":
            self.status = "Defective"
            self.price = 0
        elif self.return_reason == "In the box, like new":
            self.status = "For Sale"
        elif self.return_reason == "Opened":
            self.status = "Used"
            self.price = self.price * .2
        return self

    def display_info(self):
        print "Price: ${}".format(str(self.price))
        print "Name of Item: {}".format(str(self.item_name))
        print "Weight: {}lb".format(str(self.weight))
        print "Brand: {}".format(str(self.brand))
        print "Status: {}".format(self.status)
        print ""
        return self

product1 = Products(1000, "Elitebook", 2, "HP")
product2 = Products(234, "Headphones", 2, "Beats by Dre")
product3 = Products(567, "TV", 2, "Samsung")
product4 = Products(890, "iPhone 8", 2, "iPhone")
product5 = Products(3452, "Mystery", 2, "Mystery")

product1.item_return("Opened").display_info()
product2.item_return("In the box, like new").display_info()
product3.item_return("Defective").display_info()
product4.sell().display_info()
product5.add_tax().display_info()