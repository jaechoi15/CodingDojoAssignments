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
        print "Health:", self.health

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
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

print "*"*10 + "Animal #1" + "*"*10
animal1 = Animal("Puma")
animal1.walk().walk().walk().run().run().displayHealth()

# Unable to call the pet() method
# print "*"*10 + "Animal #2" + "*"*10
# animal2 = Animal("Daffy Duck")
# animal2.pet().displayHealth()

# Unable to call the fly() method
# print "*"*10 + "Animal #3" + "*"*10
# animal2 = Animal("Bugs Bunny")
# animal2.fly().displayHealth()

print "*"*10 + "Dog #1" + "*"*10
dog = Dog("Duke")
dog.walk().walk().walk().run().pet().displayHealth()

# Unable to call the fly() method
# print "*"*10 + "Dog #2" + "*"*10
# dog = Dog("Duke")
# dog.fly().displayHealth()

print "*"*10 + "Dragon" + "*"*10
dragon = Dragon("Toothless")
dragon.fly().displayHealth()