# (23) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string. 

# enter a string
x = input("Enter a String: ")

#  if the length of the string is less than 2
if len(x) < 2:
    y = ""  # If the string length is less than 2, return an empty string
else:
    y = x[:2] + x[-2:]  # Take the first 2 and last 2 characters and concatenate them

# Print the final result
print(y)
