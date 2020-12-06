#Error
#->syntactical error

try:
    a=int(input("enter number 1 : "))
    b=int(input("enter number 2 : "))

    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print("addition=",c)
    print("subtraction=",d)
    print("multiplication=",e)
    print("division=",f)


except BaseException as be:
    print(be)
finally:
    print("*********<><>Program Ended<><>***********")
    
    
