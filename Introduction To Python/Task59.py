# (59)Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. 

s = input("Enter a string : ")
char_count = {}
for  i in s:
    if  i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)