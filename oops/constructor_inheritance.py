# class Parent:
#   def __init__(self) -> None:
#     print("parent class constructor")

# class Child(Parent):
#   def __init__(self) -> None:
#     super().__init__()
#     print("child class constructor called")

# c = Child()    

class A:

  def feature(self):
   print("feature from a")

  def __init__(self) -> None:
    print("hey there")

class B:
  def feature(self):
   print("feature from b")

  def __init__(self) -> None:
    print("here there b")


class C(A,B):   #left to right dekhte hai inheritance mein 
  def __init__(self) -> None:
    print("hey it's c")
    super().feature()
    super().__init__()  #A wala constructor 

c = C()