# (59)Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. 

# Take user input as a string
s = input("Enter a string : ")

# Initialize an empty dictionary 
char_count = {}

for i in s:
    # If the character is already in the dictionary, increase its count
    if i in char_count:
        char_count[i] += 1
    else:
        # Otherwise, add the character with count 1
        char_count[i] = 1

# Print the dictionary containing character counts
print(char_count)
