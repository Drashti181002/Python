# (34) Write a Python function that takes two lists and returns true if they have at least one common member. 

l = [1,2,3,4]
l1 = [4,5,6,7]


for i in l:
    if i in l1:
        x = "true"
        break
    else:
        x= "false"
print(x)
