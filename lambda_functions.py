# def add(a,b):
#   return a+b

add = lambda a,b:a+b #one liner functions are basically lamda functions

print(add(2,3)) 

a = [[1,2],[3,6],[2,1]]

a.sort(key=lambda a:a[1])
print(a)