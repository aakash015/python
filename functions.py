def swap2(a,b):
  print(id(a))
  print(id(b))
  a,b = b,a
  print("inside the function")
  print(id(a))
  print(id(b))

a = 5
b = 3

swap2(a,b)

print(id(a))
print(id(b))

# def foo(a):
     
#     # A new variable is assigned
#     # for the new string
#     print(id(a))
#     a = "new value"
#     print(id(a))
#     print("Inside Function:", a)
     
     
# # Driver's code
# string = "old value"
# print(id(string))
# foo(string)
 
# print("Outside Function:", string)