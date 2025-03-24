# (35) Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

# Generate a list of squares of numbers from 1 to 30
l = [i**2 for i in range(1, 31)]  

# Print the first 5 and last 5 elements of the list
print(l[:5] + l[-5:])  
