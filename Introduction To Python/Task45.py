# (45)Write a Python program to unzip a list of tuples into individual lists. 

x1 = ('1','a','c','7',(1,2))
x2 = tuple(zip(*x1))
x2


