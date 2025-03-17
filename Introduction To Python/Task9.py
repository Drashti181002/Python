# (9) Write python program that swap two number with temp variable and without temp variable.

''' with temp'''

x = int(input("enter a number a : "))
y = int(input("enter a number b : "))

temp = x
x=y
y= temp
print("number after swapping are:" "a = ",x ,"b=",y)





''' with out temp'''

print("number before swapping are :" "a = ",x ,"b=",y)

x,y= y,x

print("number after swapping are :" "a = ",x ,"b=",y)