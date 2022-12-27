

class Computer:

  
  def config(self):
    print("this is i3 machine")


comp1 = Computer()

print(type(comp1))
print(comp1.config())
print(Computer.config(comp1))

