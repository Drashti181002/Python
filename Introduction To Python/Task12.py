# (12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# enter three integer values
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b or b == c or c == a:
    print("Sum is zero")  # If any two numbers are the same, print sum as zero

else:
    print("The sum of the numbers is:", a + b + c)  # Otherwise, calculate and print the sum
