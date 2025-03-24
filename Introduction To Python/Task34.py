# (34) Write a Python function that takes two lists and returns true if they have at least one common member. 

# Define two lists

l = [1,2,3,4]
l1 = [4,5,6,7]


for i in l:
    if i in l1:
        x = "true"    # Set x to True if a common element is found
        break
    else:
        x= "false"
print(x)  # Print the result



