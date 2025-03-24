# (54)Write a Python program to check multiple keys exists in a dictionary.

d= { 'white':1,'blue':2,'green':3}
key = ['white','blue','green']

if all(i in d for i in key):
    print(" all key are in dictionary")
else:
    print(" all key  are not in dictionary")

