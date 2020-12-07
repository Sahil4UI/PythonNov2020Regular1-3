# *args
# def Student(roll,name,*args):
#     print(roll,name,args)
# Student(10,"Sahil","10th","Delhi","98765432")

#**- keyworded argument
def Student(roll,name,**kwargs):
    print(roll,name,kwargs)
Student(10,"Sahil",Class="10th",City = "Delhi",phNo="98765432")
