# (18) Write a Python program to count occurrences of a substring in a string.

a = input("Enter a String: ")   # enter a main string
b = input("Enter a Substring: ")   # enter a substring

# Use the built-in count() method to find occurrences of the substring in the main string
count = a.count(b)

# Print the total number of times the substring appears in the main string
print("The total occurrence of the substring is:", count)
