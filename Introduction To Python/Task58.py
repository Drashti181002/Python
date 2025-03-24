# (58)Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
#Expected Output: Counter ({'item1': 1150, 'item2': 300})

# List of dictionaries containing item names and their amounts

d = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}]

d1={}   # Initialize an empty dictionary

for i in d:
    items = i["item"]    #Extract the item name
    amount = i["amount"]   #Extract the corresponding amount

    # If the item already exists in d1, add its amount
    if items in d1:
        d1[items] += amount
    else:
        # Otherwise, initialize the key with the current amount
        d1[items] = amount

# Print the final dictionary
print(d1)
