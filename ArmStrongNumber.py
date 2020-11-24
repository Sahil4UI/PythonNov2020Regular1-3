number = int(input("Enter number : "))
temp=number
Sum = 0

for i in range(len(str(number))):
    rem = number%10
    Sum += rem**3
    number = number//10

if temp == Sum:
    print("armStrong Number")
else:
    print("Not Armstrong")
