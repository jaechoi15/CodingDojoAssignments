# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

class MathDojo(object):
    def __init__(self):
        self.value = 0
        
    def add(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.value += j
            elif type(i) == tuple:
                for j in i:
                    self.value += j
            else:
                self.value += i
        return self

    def subtract(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.value -= j
            elif type(i) == tuple:
                for j in i:
                    self.value -= j
            else:
                self.value -= i
        return self

    def result(self):
        print md.value


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

md.value = 0

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()