# (60)Sample string:
# 'w3resource' Expected output: • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# Define the given string
s = "w3resource"

# Initialize an empty dictionary 
char_count2 = {}

for j in s:
    # If the character is already in the dictionary, increase its count
    if j in char_count2:
        char_count2[j] += 1
    else:
        # Otherwise, add the character with count 1
        char_count2[j] = 1

# Print the dictionary containing character counts
print(char_count2)
