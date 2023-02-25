
# details = ["aakash",1,"aakash",2]

# print(details)
# for i in details:
#   print(i,end=" ")

#   lists can be indexed as well

# print(details[1])

# lists can be sliced as well similar to string
# lists are basically arrays

n = int(input("enter size"))

sample = []

for i in range(n):
   sample.append(int(input()))

print(sample)

#deleting elements

del sample[1]
print(sample)
# del sample   deleting the list
# print(sample)