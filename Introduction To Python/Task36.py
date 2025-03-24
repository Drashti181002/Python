# (36) Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Define a list with duplicate elements
l1 = [1, 2, 3, 4, 3, 2, 5, 'a', 'b']

l2 = list(set(l1))  # Convert back to a list 

# Print the new list with unique elements
print("List with unique elements:", l2)
