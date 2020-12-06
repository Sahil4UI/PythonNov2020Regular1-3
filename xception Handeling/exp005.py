def atm():
    total=20000
    pin = input("Input Pin : ")

    if pin == "1234":
        print("you have successfully logged in")
    else:
        raise ValueError("Invalid Pin")

    amount=int(input("Enter amount to withdraw : "))

    if amount > total:
        raise ValueError("Insufficient balance")
    else:
        total = total-amount
        print("remaining balance : ",total)
        print("Collect your Cash")

try:
    atm()
    
except ValueError as err:
    print(err)
    atm()
