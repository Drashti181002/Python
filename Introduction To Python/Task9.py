# (9) Write python program that swap two number with temp variable and without temp variable.

''' with temo'''

x = int(input("Enter a number a: "))
y = int(input("Enter a number b: "))

temp = x  # Store the value of x in temp
x = y     # Assign the value of y to x
y = temp  # Assign the value of temp (which holds x) to y

# Print the swapped values
print("Numbers after swapping are: a =", x, "b =", y)



'''without temp'''

# Print the numbers before swapping
print("Numbers before swapping are: a =", x, "b =", y)

x, y = y, x  # Swap values directly

# Print the swapped values
print("Numbers after swapping are: a =", x, "b =", y)
