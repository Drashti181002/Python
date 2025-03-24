# (41)Write a Python program to check whether a list contains a sub list. 

l1 = [1,2,3,4,5,6,7] # Define the main list

l2 = [9,7]  # Define the sublist to check

# Check if all elements of l2 are present in l1

for i in l2:
    if i in l1:
        print("sub list")
        
    else:
        print("not sub list")



