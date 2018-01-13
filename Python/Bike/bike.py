class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: {}; Max Speed: {}; Total Miles {}".format(str(self.price), str(self.max_speed), str(self.miles))
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 10
        return self

bike1 = Bike(200, "25 mph")
bike2 = Bike(100, "40 mph")
bike3 = Bike(300, "123 mph")

# Total Miles will display 20
bike1.ride().ride().ride().reverse().displayInfo()
# Total Miles will display 0
bike2.ride().ride().reverse().reverse().displayInfo()
# Total Miles will display -30
bike3.reverse().reverse().reverse().displayInfo()
