# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *args):
        for i in args:
            if type(i) == list:
                for j in i:
                    self.value += j
            else:
                self.value += i
        return self
    
    def subtract(self, *args):
        for i in args:
            if type(i) == list:
                for j in i:
                    self.value -= j
            else:
                self.value -= i
        return self
    
    def displayResult(self):
        print "Result:", self.value

print "*"*10 + "Part I" + "*"*10
md1 = MathDojo()
md1.add(2).add(2,5).subtract(3,2).displayResult()

print "*"*10 + "Part II" + "*"*10
md2 = MathDojo()
md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).displayResult()