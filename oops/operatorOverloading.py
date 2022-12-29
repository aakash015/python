#behind the scene + call __add__ method 
#similarly - call __sub__ method
# these are reffered as magic methods

class Student:

  def __init__(self,m1,m2) -> None:
    self.m1 = m1
    self.m2 = m2

  def __add__(self,s2):
    return [self.m1+s2.m1,self.m2+s2.m2]
  
  def __gt__(self,s2):
    if (self.m1+self.m2)>(s2.m1+s2.m2):
      return True
    else:
      return False  
  
s1 = Student(10,20)
s2 = Student(20,30)

print(s1+s2)

if s1>s2:
  print("s1")
else:
  print("s2")  