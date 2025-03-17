# (64)Write a Python function that checks whether a passed string is palindrome or not.

def fun(x):
    return x == x[::-1]

x = input("Enter a string : ")

if fun(x):
    print("it is palindrome")
else:
    print("it is bot palindrome")