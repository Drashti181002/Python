# (40)Write a Python program to get unique values from a list.

# Define a list with duplicate values
l1 = [1, 2, 4, 3, 4, 5, "a", "a", "a"]

# Convert the list into a set to remove duplicates
l2 = set(l1)

# Print the unique values
print("Unique List =", l2)
