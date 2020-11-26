x=[90,87,56,-1000,789,43,32,-90,-87]
x=sorted(x)
print(x)
user = int(input("Enter Number : "))

#binarySearch
left =0
right = len(x) - 1
found = False
while left <= right:
    mid = (left+right)//2
    if x[mid] > user:
        right = mid-1
    elif x[mid] < user:
        left = mid+1
    elif x[mid]==user :
        found=True
        print("Found=",x[mid])
        break


if found ==False:
    print("not found")
