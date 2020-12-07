def f1():
    print("i am inside f1")
    def f2():
        print("i am inside f2")
    def f3():
        print("I am inside f3")
    def f4():
        print("i am inside 4")
    
    return f2,f3,f4

x,y,z = f1()
x()
y()
z()