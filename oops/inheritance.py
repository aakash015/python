class Parent:

  

  def feature1(self):
    print("hey there feature 1")

  def feature2(self):
    print("hey there feature 2")

class Child(Parent):  #single inheritance

  def feature3(self):
    print("hey there feature 3")

  def feature4(self):
    print("hey there feature 4")

#multilevel inheritance

class Grandchild(Child):
   def feature5(self) -> None:
    print("5th feature called")

# class Seperate:
#   def feature6():
#     print("this is feature6 by sepearte class")

#multiple inheritance 

# class test(Seperate,Parent):
#   def feature7():
#     print("hello from multiple inheritance")

c = Parent()
c.feature1()

gc = Grandchild()
gc.feature5()

# t = test()
# t.feature1()


