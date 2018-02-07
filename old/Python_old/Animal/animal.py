# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal's Name: {}".format(str(self.name))
        print "Remaining Health: {}".format(str(self.health))
        print ""
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print "Animal's Name: {}".format(self.name)
        print "Remaining Health: {}".format(self.health)
        print "I am a Dragon!"
        print ""
        return self

animal1 = Animal("Bear")
animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("Duke")
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Toothless")
dragon1.walk().run().fly().displayHealth()

# This instance will return an error since fly() is not a method for hte Dog object.
# dog2 = Dog("Bailey")
# dog2 = fly().displayHealth()

# This instance will return an error since pet() is not a method for hte Dragon object.
# dragon2=Dragon("Bob")
# dragon2.pet().displayHealth()