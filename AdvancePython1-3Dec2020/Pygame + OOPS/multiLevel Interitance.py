import random
class Bank:
    customers = []
    def __init__(self):
        self.bank = "IDFC"
        self.branch = "Rohini"
        self.ifsc = "IDF009"
        self.accNo = random.randint(1000,10000)
        self.currentUser = {}


    def storeDefault(self):
        self.currentUser['account_num'] = self.accNo
        self.currentUser['branch'] = self.branch
        self.currentUser['IFSC'] = self.ifsc
        self.customers.append(self.currentUser)

    
    def showAll(self):
        print(self.customers)
        


class Customer(Bank):
    def __init__(self,name,age,occ):
        self.cust_name = name
        self.cust_age = age
        self.occ =occ
        super().__init__() #calling parent class constructor

    def storeCustomer(self):
        self.currentUser['name'] = self.cust_name
        self.currentUser['age'] = self.cust_age
        self.currentUser['occupation'] = self.occ

    def showCurrentCustomer(self):
        print("Welcome to IDFC bank")
        print("Branch : ",self.branch)
        print("Details of customer : ")
        print(self.currentUser)
        print("************************")


class Employees(Customer):
    def __init__(self,name,age,occ):
        self.name = name
        self.age = age
        self.occ = "Emp"
        self.acc_type = acc_type
        self.sal = sal
        super().__init__(self.name,self.age,self.occ) #calling parent class constructor

    def storeEmp(self):
        self.currentUser['salary'] = self.sal
        self.currentUser['acc_type'] = self.acc_type


    #overriding    
    def showCurrentCustomer(self):
        print("Welcome to IDFC bank")
        print("Branch : ",self.branch)
        print("Details of customer : ")
        print(self.currentUser)
        print("************************")
