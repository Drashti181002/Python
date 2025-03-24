# (62)Write a Python function to check whether a number is in a given range.
 
def r(start,x,end,):
    return start <= x <= end   # Returns True if x is within the range, else False

start = int(input("Enter start a number : "))
end = int(input("Enter end number : "))
x = int(input("Enter a number : "))
print(r(start,x,end))


