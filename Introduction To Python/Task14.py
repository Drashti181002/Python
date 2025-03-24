# (14) Write a python program to sum of the first n positive integers. 

n = int(input("Enter a Number: "))

# Initialize sum variable to store the total sum
sum = 0  

for i in range(1, n + 1):  # Loop from 1 to n
    sum += i  # Add the current number to sum

print(sum)  # Print the final sum

