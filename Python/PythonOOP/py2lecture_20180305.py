class Electronic(object):
    def __init__(self, materials=["metals", "copper", "transistors"], plugType="3 prong"):
        self.plugType = plugType
        self.materials = materials
    def printSelf(self):
        print self.plugType
        print self.materials

class Computer(Electronic):
    def __init__(self, color, RAM, CPU, harddrive):
        super(Computer, self).__init__()
        self.color = color
        self.RAM = RAM
        self.CPU = CPU
        self.harddrive = harddrive
    def printSelf(self):
        super(Computer, self).printSelf()
        print self.harddrive
        print self.color
        print self.RAM
        print self.CPU

myComputer = Computer("silver",8,"Intel i7","512GB SSD")
print myComputer["harddrive"]
# myComputer = Computer("silver", 8, "Intel i7", "512GB SSD")
# print myComputer
# myComputer.printSelf()

# yourComputer = Computer("black", 8, "Intel i7", "1024GB SSD")
# print yourComputer
# yourComputer.printSelf()