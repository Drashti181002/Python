# (20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 


# enter the first string
x19 = input("Enter the 1st string: ")

# enter the second string
x20 = input("Enter the 2nd string: ")

# Swap the first two characters of each string
p = x20[:2] + x19[2:]  
q = x19[:2] + x20[2:]  

# Combine both modified strings with a space in between
x21 = p + " " + q

# Print the final result
print(x21)
