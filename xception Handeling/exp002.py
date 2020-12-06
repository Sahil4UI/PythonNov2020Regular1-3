#Error
#->syntactical error

try:
    a=int(input("enter number 1 : "))
    b=int(input("enter number 2 : "))

    c=a+b
    d=a-b
    e=a*b
    f=a/b
    

except BaseException as be:
    print(be)
else:
    print("addition=",c)
    print("subtraction=",d)
    print("multiplication=",e)
    print("division=",f)

    
