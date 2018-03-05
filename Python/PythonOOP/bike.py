# Create a new class called Bike with the following properties/attributes:
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
# Add the following functions to this class:
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "Price: $", str(self.price)
        print "Maximum Speed: " + str(self.max_speed) + " mph"
        print "Miles: " + str(self.miles) + " miles"
    
    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0

print "*"*10 + "Bike 1" + "*"*10
bike1 = Bike(5,25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

print "*"*10 + "Bike 2" + "*"*10
bike2 = Bike (10,40)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

print "*"*10 + "Bike 3" + "*"*10
bike3 = Bike(5,25)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()