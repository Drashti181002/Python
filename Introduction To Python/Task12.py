# (12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
c = int(input("enter a third number : "))

if a==b or b==c or c==a:
    print("sum is zero")
else:
    print("the sum of the numbers is :",a+b+c)
    