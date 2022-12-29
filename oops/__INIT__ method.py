

class Computer:

  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram
    # print(cpu," ",ram)   #this method is getting called automatically once object is created
    # print("inside init method")

  def config(self):
    print("config is ",self.cpu," ",self.ram)

  def compare(self,c2):
    if self.ram==c2.ram and self.cpu==c2.cpu:
      print("they are equal")
    else:
      print("they are not equal")  


C1 = Computer('i5','65')
C2 = Computer('i3','65')
# C1.config()

# print(C1.cpu)
# print(id(C1))
# print(id(C2))
C1.compare(C2)

if(C1.ram==C2.ram):
  print("test")

#for comparing two objects 
# 

