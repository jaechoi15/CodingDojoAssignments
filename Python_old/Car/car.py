# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
            
        self.display_all()

    def display_all(self):
        print "Price: ${} Speed: {}mph; Fuel: {}; Mileage: {}mpg; Tax: {}".format(str(self.price), str(self.speed), str(self.fuel), str(self.mileage), str(self.tax))
        return self

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000000, 35, "Empty", 15)