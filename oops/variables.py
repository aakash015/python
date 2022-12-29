
#we have two namespaces 
#1.class namespae 
#2.instance namespace

class Car:

  wheels = 5 #this is a class or static variable
  def __init__(self):
    self.mil=10,
    self.com = "BMW"


c1 = Car()
c2 = Car()
# c1.wheels=2
print(c1.wheels)
print(Car.wheels)
