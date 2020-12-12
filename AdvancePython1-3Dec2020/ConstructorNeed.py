class Bank:
    acc_no = None
    bal = 0
    pin = None
    branch = "Rohini"
    ifsc = "kkbk0007"

    details=[]

    def showDetails(self):
        # self -> refers to current object
        print("*****Details*****")
        self.details.append([self.acc_no,self.bal,self.pin,self.branch,self.ifsc])
        print(self.details)

    def InputDetails(self):
        pass

customer1 = Bank()
customer1.acc_no = 1012345
customer1.bal = 21343
customer1.pin = 1234
customer1.showDetails()


customer2 = Bank()
customer2.acc_no = 106576
customer2.bal = 9876
customer2.pin = 12734
customer2.showDetails()