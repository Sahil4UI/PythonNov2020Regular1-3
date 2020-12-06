#Error
#->syntactical error

try:
    a=int(input("enter number 1 : "))
    b=int(input("enter number 2 : "))

    c=a+b
    print("addition=",c)

    d=a-b
    print("subtraction=",d)


    e=a*b
    print("multiplication=",e)


    f=a/b
    print("division=",f)

except BaseException as be:
    print(be)
    
'''
except ZeroDivisionError:
    print("Number cannot be divided by zero")

except ValueError:
    print("Invalid Value")
'''
