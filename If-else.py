#Find the largest b/w 2
'''
x = int(input("Enter Number1 :"))
y = int(input("Enter Number2 :"))

if x>y:
    print(f" {x} is largest")
else:
    print(f" {y} is largest")
'''

'''
#fIND the largest b/w three no's
x = int(input("Enter Number1 :"))
y = int(input("Enter Number2 :"))
z = int(input("Enter Number3 :"))

if x>y and x>z:
    print(f" {x} is largest")
elif y>z:
    print(f" {y} is largest")
else:
    print(f" {z} is largest")
'''
#Check wether no is even or odd
'''
# find no is even or odd

x = int(input("enter no.1"))

if x%2 ==0:
    print("Even")
else:
    print("Odd")
'''
#check whether the triangle is equilateral, isoceles, scalene

x = int(input(" enter no.1"))
y = int(input("enter no.2"))
z = int(input("enter no.3"))

if x+y>z and y+z>x and z+x>y:    
    if x==y and y==z:
        print("Equilateral")
        
    elif x==y or y==z or z==x:
        print("isoceles")
        
    else:
        print("scalene")
else:
    print("Invalid Sides")
