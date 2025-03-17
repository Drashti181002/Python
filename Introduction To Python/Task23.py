# (23) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string. 

x = input("Enter a String : ")

if len(x)<2:
    print("")
else:
    y = x[:2]+x[-2:]
y