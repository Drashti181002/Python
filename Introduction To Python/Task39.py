# (39)Write a Python program to find the second smallest number in a list. 

# Define a list of numbers
l1 = [1, 2, 3, 5]

# Remove the smallest number from the list
l1.remove(min(l1))

# Find the new smallest number
l2 = min(l1)

# Print the second smallest number
print(l2)
