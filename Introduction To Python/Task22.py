# (22) Write a Python function to reverses a string if its length is a multiple of 4. 

# enter a string
n = input("Enter a String: ")

# Check if the length of the string is a multiple of 4
if len(n) % 4 == 0:
    n = n[::-1]  # Reverse the string if its length is a multiple of 4

# Print the final result
print(n)
