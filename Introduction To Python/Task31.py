# (31) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a
#given list of strings.

'''pending'''
count = 0   # Initialize a count variable to track valid strings

n = ['abc','vfe','gfgfd','asd']   # Define a list of strings

if len(n)>=2 or n[0]==n[-1]:
    count+=1   # Increment the count if the condition is met

    print(count)
 

