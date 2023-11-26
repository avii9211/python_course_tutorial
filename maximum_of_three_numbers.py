#write a python program to find the maximum of three numbers 

a = int(input("Enter first number"))
b = int(input("Enter second number "))
c=int(input("Enter third number"))

# logic for finding maximum of three numbers 
if a > b :
    if a > c :
        print(a,"is maximum")
    else:
        print(c,"is maximum")
elif b >  a :
    if b > c :
        print(b,'is maximum')
    else:
        print(c,'is maximum')
else:
    print(c,'is maximum')