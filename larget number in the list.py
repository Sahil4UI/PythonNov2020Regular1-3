'''
x=[90,87,56,-1000,789,43,32,-90,-87]
largest = -9999999999999
secondLargest=-999999
for value in x:
    if largest < value:
        largest,secondLargest=value,largest
    elif secondLargest < value:
        secondLargest = value
        

print("LArgest=",largest)
print("Second LArgest=",secondLargest)

#remove dup from list-[1,2,3,4,5,6]
x=[1,1,1,2,2,3,3,4,4,4,5,6]
y=[]
for value in x:
    if value not in y:
        y.append(value)

print(y)
'''
'''
#[90,87,56,-1000,789,43,32,-90,-87] ->sort
x=[90,87,56,-1000,789,43,32,-90,-87]

for i in range(len(x)):
    minValueIndex = i
    for j in range(i+1,len(x)):
        if x[minValueIndex] > x[j]:
            minValueIndex=j
    x[i],x[minValueIndex] =  x[minValueIndex],x[i]
print(x)
'''
"""
x=[1,1,1,2,2,3,3,4,4,4,5,6,7,8,8,9,9]
#find the first unique element from the list
for i in x:
    if x.count(i)==1:
        print(i)
"""
#Linear Search Algorithm
x=[90,87,56,-1000,789,43,32,-90,-87]
x= x.sort()
user = int(input("Enter Number : "))

#binarySearch
left =0
right = len(x) - 1

while left <=right:
    mid = (left+right)//2

    if x[mid] > user:
        right = mid-1
    elif x[mid] < user:
        left = mid+1
    else:
        print(x[mid])
        

    
    
    














"""
if user in x:
    print("found")
else:
    print("not found")
"""
"""
for i in range(len(x)):
    if user == x[i]:
        print("found")
        break
else:
    print("not found")

"""

















        
