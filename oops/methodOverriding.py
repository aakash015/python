class A:

  def show(self):
    print("show A")

class B(A):

  def show(self):
    print("show B")

b = B()    
b.show()