# (11) Write a Python program to test whether a passed letter is a vowel or not. 

n = input("Enter a letter : ")

if n in 'AEIOUaeiou':   # Check if the entered letter is a vowel (both uppercase and lowercase)
    print("Letter is a vowel")  # Print message if the letter is a vowel
    
else:
    print("Letter is not a vowel")  # Print message if the letter is not a vowel
