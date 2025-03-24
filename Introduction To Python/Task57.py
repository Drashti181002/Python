# (57)Write a Python program to find the highest 3 values in a dictionary.

# Define a dictionary with key-value pairs
d = {'a' : 100,'b' : 200,'c' : 600,'d' : 900,'e' : 500,'f' : 800}
lst = list(d)
lst.sort()
print("the highest three value is : ",lst[3:])