# (13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

x = int(input("enter a first number : "))
y = int(input("enter a second number : "))

if x==y or x+y==5 or x-y==5:
    print("true")
else:
    print("false")