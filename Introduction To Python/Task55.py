# (55)Write a Python script to merge two Python dictionaries.

def merge(d1,d2):
    return(d1.update(d2))  # Explicitly return the merged dictionary
d1 = {1,2,3,4}
d2={'a','b'}
merge(d1,d2)
d1


