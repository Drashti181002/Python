# (6) Write a Python program to get the Fibonacci series of given range. 

n = int(input("Enter Terms : "))

# Initialize the first two terms of the Fibonacci sequence
n1 = 0  
n2 = 1  

# Print the first two terms
print(n1)  
print(n2)  

for i in range(3, n + 1):  
    n3 = n1 + n2  # Calculate the next term in the sequence
    print(n3)  # Print the current Fibonacci number
    n1 = n2  # Update n1 to the previous n2
    n2 = n3  # Update n2 to the newly calculated n3
