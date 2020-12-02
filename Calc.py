def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

a = int(input("Enter value 1:"))
b = int(input("Enter value 2:"))

print(""""
Press + for addition
Press -  for subtraction
Press *  for multiplication
Press /  for Division
""")

    
choice = input("Enter Choice : ")
d = {"+":add,"-":sub,"*":mul,"/":div}
d.get(choice)(a,b)

