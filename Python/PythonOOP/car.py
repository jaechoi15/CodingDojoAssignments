# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    
    def display_all(self):
        print "Price: $", self.price
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + " mpg"
        print "Tax: " + str(self.tax)

print "*"*10 + "Car 1" + "*"*10
car1 = Car(2000, 35, "Full", 15)
car1.display_all()

print "*"*10 + "Car 2" + "*"*10
car1 = Car(5000, 5, "Not Full", 105)
car1.display_all()

print "*"*10 + "Car 3" + "*"*10
car1 = Car(8000, 45, "Kind of Full", 20)
car1.display_all()

print "*"*10 + "Car 4" + "*"*10
car1 = Car(20000, 100, "Full",25)
car1.display_all()

print "*"*10 + "Car 5" + "*"*10
car1 = Car(10000, 65, "Empty", 35)
car1.display_all()

print "*"*10 + "Car 6" + "*"*10
car1 = Car(70000, 150, "Full", 100)
car1.display_all()