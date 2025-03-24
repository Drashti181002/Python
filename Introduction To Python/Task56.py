# (56)Write a Python program to map two lists into a dictionary 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

key = ['a','b','c']
value = [1,2,3]
d = {}
for  i in range(len(key)):
    d[key[i]] = value[i]
print(d)


