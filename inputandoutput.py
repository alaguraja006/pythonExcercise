print()
print("Hello" *3)
print("This is my sample\n program.")

a,b=10,20
print(a,b)
print(a,b,sep=",")

marks=94.87333
name="sanjay"

print(name,marks)
print("Name is",name,"Marks are",marks)
print("Name is %s,Marks are %.2f"%(name,marks))
print("Name is {},Marks are {}".format(name,marks))
print("Name is {0},Marks are {1}".format(name,marks))

s=input()
print(s)
s=input("Enter your Name:")
print(s)
i = int(input("Enter the integer :"))
print(i)
lst = [x for x in input("enter three number seperate by spaces:").split()]
print(lst)
lst = [x for x in input("enter three number seperate by comma:").split(',')]
print(lst)


