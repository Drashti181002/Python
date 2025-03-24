# (24) Write a Python function to insert a string in the middle of a string.

# enter the first string
x = input("Enter the 1st string: ")

# enter the second string 
y = input("Enter the 2nd string: ")

# Find the middle index of the first string
z = len(x) // 2

# Insert the second string into the middle of the first string
x2 = x[:z] + " " + y + " " + x[z:]  # Adding spaces 

# Print the final string
print(x2)
