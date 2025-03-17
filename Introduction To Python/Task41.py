# (41)Write a Python program to check whether a list contains a sub list. 

l1 = [1,2,3,4,5,6,7]
l2 = [9,7]

for i in l2:
    if i in l1:
        print("sub list")
        
    else:
        print("not sub list")
