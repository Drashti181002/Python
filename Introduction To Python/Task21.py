#(21) Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then
# add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

n = input("Enter a Word :")

if len(n)<3:
    result = n
elif n.endswith("ing"):
    result = n+"ly"
else:
    result = n+"ing"
print(result)
    
