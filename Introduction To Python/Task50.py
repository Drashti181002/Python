# (50)Write a Python script to check if a given key already exists in a dictionary. 

d = { 'white':1,'blue':2,'green':3}

i = input("Enter a key : ")

if i in d:
    print("key is in dictionary")
else:
    print("key is  not in dictionary")