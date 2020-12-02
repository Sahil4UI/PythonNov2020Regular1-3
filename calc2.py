def calc(x,y,opr):
    result = x+opr+y
    print(eval(result))
    
a = input("Enter value 1:")
b = input("Enter value 2:")

print("""
Press + for addition
Press -  for subtraction
Press *  for multiplication
Press /  for Division
""")

choice = input("Enter Choice : ")
calc(a,b,choice)


