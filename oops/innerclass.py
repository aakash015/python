class Student:
  
  class laptop:
    def __init__(self,ram,cpu) -> None:
       self.ram = ram
       self.cpu = cpu
         
  def __init__(self,name,rollno,ram,cpu) -> None:
    self.name = name
    self.rollno = rollno
    self.lap = self.laptop(ram,cpu)

  def display(self):
    print(self.rollno+" "+self.name+" "+self.lap.cpu+" "+self.lap.ram)

s1 = Student("aakash","2","14","i3")
s2 = Student("varad","22","16","i2")

s1.display()



