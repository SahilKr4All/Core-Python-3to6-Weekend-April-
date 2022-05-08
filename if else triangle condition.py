# check whether the triangle is or not

x = int(input("enter no.1"))
y = int(input("enter no.2"))
z = int(input("enter no.3"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        print("equilateral")
    elif x==y or y==z or z==x:
        print("isoceles")
    else :
        print("scelene")
else:
    print("is invalid")
        
