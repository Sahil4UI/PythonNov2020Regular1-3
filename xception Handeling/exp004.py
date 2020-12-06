def atm():
    total=10000
    pin = input("Enter you debit card pin")
    if pin =="1234":
        print("Login Successfull")
    else:
        raise ValueError("Login Failed")

    amount = int(input("Enter amount to withdraw"))
    if amount > total:
        raise ValueError("Insufficient Balance")
    else:
        total-=amount
        print(f"Remaining Balance is : {total}")

try:
    atm()
    
except ValueError as err:
    print(err)
    atm()
