#strings are immutable in python

name = "Aakash"
about = '''Aakash is a very nice person.
he loves to eat sleep repeat'''
print(name)
print(about)
print(name[-1])
print(name[0])
s = name[::-1]
print(s)
# s = name.split('')
print(s)

# slicing in python
# s = name[0:3]
# s = name[-1:-4:-1]
# print(s)

s = name[0:10] #would not produce an error
print(s)

s = name[0:] #by default end of string
print(s)

 #by default start of string
print(name[:3])

#right to left jaana hai na isliye negative indexing kaam ayegi
print(name[4:2:-1]) # sa as output

print("abc"+"bca")
print("abc"*2)

for i in name:
  print(i,end=' ')


print(f"my name is {name}")
# s[3] = 'x'
# print(s) will give error as strings are immutable 

