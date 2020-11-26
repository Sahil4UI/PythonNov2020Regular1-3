'''
x = int(input("Enter a Number : "))
i=2
while i<x:
    if x%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")
'''

#1-100
x1= 2
isPrime =True
while x1<=100:
    for i in range(2,x1):
        if x1%i==0:
            isPrime=False
            break
            
    
    else:
        print(x1)
    x1+=1
        
    
