import datetime
class Bank:
    bname="SBI"#bname is a static variable
    def createAccount(self,acno):
        self.minimumbal=3000
        self.bal=self.minimumbal
        self.acno=acno

    def withDraw(self):
        amnt = int(input("enter the the amount you want to withdraw"))
        self.bal-= amnt
        print("your",Bank.bname," account no",self.acno,"has been withdrew with amnt",amnt,"on",datetime)
        print("your available balance=", self.bal)

    def deposit(self):
        amnt=int(input("enter the the amount you want to deposit"))
        self.bal+=amnt
        print("your",Bank.bname,"account no",self.acno, "has been deposited with amnt",amnt,"on",datetime)
        print("your available balance=",self.bal)


obj=Bank()
obj.createAccount(10002)
obj.withDraw()
obj.deposit()

obj1=Bank()
obj.createAccount(10005)
obj.withDraw()
obj.deposit()
