# (90)Write python program that user to enter only odd numbers, else will raise an exception. 

try:
    n = int(input("Enter odd number : "))

    if n % 2 == 0:
        raise (ValueError("Odd numbers are allowed!"))
    
    print(f"odd number: {n}")

except ValueError:
    print(ValueError)









