#(19) Write a Python program to count the occurrences of each word in a given sentence.

'''(pending)'''
a = input("Enter a sentence: ")   # enter a sentence

words = a.split()  # using the split() method
word_count = {} # Create an empty dictionary 


for word in words:
    # If the word is already in the dictionary, increase its count
    if word in word_count:
        word_count[word] += 1
    else:
        # If the word is not in the dictionary, add it with count 1
        word_count[word] = 1


