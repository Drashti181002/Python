# (22) Write a Python function to reverses a string if its length is a multiple of 4. 

n = input("Enter a  String : ")

if len(n) %4 == 0:
    n= n[::-1]
n