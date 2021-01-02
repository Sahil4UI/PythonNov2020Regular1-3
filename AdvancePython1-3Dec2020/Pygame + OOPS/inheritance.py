import random
class Bank:
    def __init__(self):
        self.bank = "IDFC"
        self.branch = "Rohini"
        self.ifsc = "IDF009"
        self.accNo = random.randint(1000,10000)
        self.customer =[]


    def storeCustomer(self):
        self.customer.append([self.accNo,self.branch,self.ifsc])


class Customer(Bank):
    def __init__(self,name,age,occ):
        self.cust_name = name
        self.cust_age = age
        self.occ =occ
        super().__init__() #calling parent class constructor

    def show(self):
        print("Welcome to IDFC bank")
        print("Branch : ",self.branch)
        print("acc No : ",self.accNo)
        print("Details of customer : ")
        self.customer.append([self.cust_name,self.cust_age,self.occ])
        print(self.customer)
        print("************************")

obj = Customer("shyam",35,"Accountant")
obj.storeCustomer()
obj.show()