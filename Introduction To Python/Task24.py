# (24) Write a Python function to insert a string in the middle of a string.

x = input("Enter a 1st string : ")
y = input("Enter a 2nd string : ")

z = len(x)//2
x2 = x[:z]+ " " + y +x[z:]
x2