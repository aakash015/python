a = 5
b = 0

try:
  print("file open")
  print(a/b)
except Exception as e:
  print(e)  
finally:
  print("file closed")