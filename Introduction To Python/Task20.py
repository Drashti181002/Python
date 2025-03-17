# (20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

x19 = input("Enter a 1st string : ")
x20 = input("Enter a 2nd string : ")

p= x20[:2] + x19[2:]
q= x19[:2] + x20[2:]
x21= p + " "+ q
x21
