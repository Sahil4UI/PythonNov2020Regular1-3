class Bank:
    branch = "Rohini"
    ifsc = "kkbk0007"

    #constructor
    def __init__(self,name,acc_no,bal,pin):
        self.name = name
        self.acc_no = acc_no
        self.bal = bal
        self.pin = pin
        self.details=[]

    def showDetails(self):
        # self -> refers to current object
        print("*****Details*****")
        self.details.append([self.acc_no,self.bal,self.pin,self.branch,self.ifsc])
        print(self.details)
        #destructor
    def __del__(self):
        print(f"Object of {self.name} destroyed ")



customer1 = Bank("Sahil",1012345,21343,1234)
customer1.showDetails()


customer2 = Bank("Rajesh",106576,9876,12734)
customer2.showDetails()