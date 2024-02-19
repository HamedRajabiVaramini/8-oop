'''
simple_programming_

This code defines Book class 
with to string method 
'''
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name:{self.first_name} {self.last_name}"

print(Person("Hamed", "Rajabi"))
# output: Name:Hamed Rajabi


