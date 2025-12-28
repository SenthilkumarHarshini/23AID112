print("Enter any two numbers of your choice.")
a=input("Number 1:")
b=input("Number 2:")
a_int=int(a)
b_int=int(b)
SUM=a_int+b_int
DIFF=a_int-b_int
PRODUCT=a_int*b_int
print("The sum of the two numbers is",SUM)
print("The difference of the two numbers is",DIFF)
print("The product of the two numbers is",PRODUCT)
if (a>b):
    print(a_int,"is the bigger number.")
elif (a<b):
    print(b_int,"is the bigger number.")
else:
    print("The two numbers are equal.")