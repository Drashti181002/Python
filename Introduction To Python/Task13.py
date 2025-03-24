# (13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

# enter two integer values
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x == y or x + y == 5 or abs(x - y) == 5:    # Check if the two numbers are equal, their sum is 5, or their difference is 5
    print("True")  # Return true if any of the conditions true
else:
    print("False")  # Return false otherwise
