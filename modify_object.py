'''
simple_programming_

This code defines Book class 
with to string method 
'''
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def isTall(self):
        if self.height > 180:
            return True
        return False

p1 = Person("Person#1", 170)
print(p1.isTall())
# output: False
p1.height = 185
print(p1.isTall())
# output: True



