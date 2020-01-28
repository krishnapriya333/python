class Person:
    def createAccount(self,bname,acno,bal):
        self.bal=bal
        self.bname=bname
        self.acno=acno

    def withDraw(self,amnt):
        self.amnt=amnt
        self.bal-=amnt
    def deposit(self,amnt):
        self.amnt=amnt
        self.bal+=amnt
    def balEnq(self):
        print(self.bname)
        print(self.acno)
        print(self.bal)



obj=Person()
obj.createAccount("SBI",123,10000)
obj.withDraw(5000)
obj.deposit(6000)
obj.balEnq()



obj1=Person()
obj1.createAccount("ICICI",456,20000)
obj1.withDraw(5000)
obj1.deposit(6000)
obj1.balEnq()



