# (48)Write a Python script to sort (ascending and descending) a dictionary by value. 

# Define a dictionary with key-value pairs
dic = {1: 50, 2: 20, 3: 80, 4: 10, 5: 30}

# Sort dictionary in ascending order
sorted_asc = dict(sorted(dic.items(), key=lambda item: item[1]))

# Sort dictionary in descending order 
sorted_desc = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

# Print outputs
print("Ascending Order:", sorted_asc)
print("Descending Order:", sorted_desc)
