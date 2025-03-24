# (5) Write a Python program to get the Factorial number of given numbers. 

n = int(input("Enter number : "))
 
i = 1      # variable starting from 1
fac = 1    # Variable to store the factorial result, initialized to 1

while i <= n:
    fac *= i  # Multiply fac by the current value of i
    i = i + 1  # Increment i

print("Factorial number is : ",fac)


