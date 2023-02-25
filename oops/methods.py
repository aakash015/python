#we have instance method , class method, static method
#class and static methods are different 

class Student:
  
  school = "gps"
  def __init__(self,m1,m2,m3) -> None:
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  @classmethod #decorator  #iske bina ye info method error dega
  #it can modify class method
  def info(k):
   k.school = "dcx" 
   return k.school

# when we are not concerned about instance variable and class variable then 
# static variables comes into picture
  @staticmethod
  def ram():
   print("ram ram jai raja ram")
   

s1 = Student(2,3,4)
s2 = Student(5,6,7)
s3 = Student(1,2,3)

print(Student.info())
print(s2.school)
print(Student.ram())