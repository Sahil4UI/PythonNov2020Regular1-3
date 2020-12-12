class Bank:
    branch = "Rohini"
    ifsc = "kkbk0007"

    #constructor
    def __init__(self):
        self.name = None
        self.acc_no = None
        self.bal = 0
        self.pin = None
        self.details=[]

    def showDetails(self):
        # self -> refers to current object
        print("*****Details*****")
        self.details.append([self.acc_no,self.bal,self.pin,self.branch,self.ifsc])
        print(self.details)
        #destructor
    def __del__(self):
        print(f"Object of {self.name} destroyed ")



customer1 = Bank()
customer1.name = "Sahil"
customer1.acc_no = 1012345
customer1.bal = 21343
customer1.pin = 1234
customer1.showDetails()


customer2 = Bank()
customer2.name ="Rajesh"
customer2.acc_no = 106576
customer2.bal = 9876
customer2.pin = 12734
customer2.showDetails()