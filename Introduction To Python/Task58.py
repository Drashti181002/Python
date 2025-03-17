# (58)Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
#Expected Output: Counter ({'item1': 1150, 'item2': 300})

d = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}]

d1={}
for i in d:
    items = i["item"]
    amount = i["amount"]
    if items in d1:
        d1[items] += amount
    else:
        d1[items] = amount
print(d1)