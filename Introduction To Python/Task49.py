# (49)Write a Python script to concatenate following dictionaries to create a new one. 

d1 = {'a':1,'b':2}
d2 = {'p':3,'q':4}
d3 = {'x':5,'y':6}

d4 = d1.copy()
d4.update(d2)
d4.update(d3)

print(d4)




