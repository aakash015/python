# f=open()  then this f is basically a file pointer 
#pointing to the beginning of the file and this pointer is returned by the open function

f = open('FileHandling/test.txt',mode='w') #if file don't exist then it will create the file
#by default the mode is write
if f:
  print("file opened successfully")

print(f)

#buffering argument:- kitne kitne bites ko buffer memory mein laake process krna hai
#kyunki poori ki poori file ko buffer mein laake koi benefit nahi hai ye integer hota hai

#errors :-  ismein bta skte ho ki error aaye to turant dena hai ya ignore kr dena hai

print(f.readable()) #used to check whether the file is in read mode or not 

print(f.writable())


f.close()
#jab hum file ko close krte hai to ye fileobject delete ho jaata hai aur ab file accessible nahi hai 
#garbage collector jo hai wo waise to automatically files ko close kr dega 
#but wo close krta hai jab saara ka saara program execute ho jaata hai , to ho skta hai ki kuchh 
#unexpected operations ho jaaye isliye khud hi band krna sahi hai 

print(f.name)
print(f.closed)


