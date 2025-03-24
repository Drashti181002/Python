#(21) Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then
# add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

# enter a word
n = input("Enter a Word: ")

# Check if the length of the string is less than 3
if len(n) < 3:
    result = n  # If the word has less than 3 characters, leave it unchanged
elif n.endswith("ing"):
    result = n + "ly"  # If the word already ends with 'ing', add 'ly' at the end
else:
    result = n+'ing'

print(result)
