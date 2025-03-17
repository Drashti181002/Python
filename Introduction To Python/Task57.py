# (57)Write a Python program to find the highest 3 values in a dictionary.

d = {100,200,600,900,500,800}
lst = list(d)
lst.sort()
print("the highest three value is : ",lst[3:])