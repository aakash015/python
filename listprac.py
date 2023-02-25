lis = []

x = int(input("enter the size of the list \n"))

for i in range(0,x):
  lis.append(int(input()))

lis[1] = 'a'

print(lis)
