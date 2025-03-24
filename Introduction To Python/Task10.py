# (10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 

n = int(input("Enter a Number : "))

if n % 2 == 0:   # Check if the number is divisible by 2 
    print("Number is Even")  # Print message if the number is even

else:
    print("Number is Odd")  # Print message if the number is odd
