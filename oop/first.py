class Student:
    def setValues(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def printValues(self):
        print(self.name)
        print(self.age)
        print(self.mark)

obj=Student()
obj.setValues("krishna",25,78)
obj.printValues()

obj1=Student()
obj1.setValues("laya",28,80)
obj1.printValues()

obj2=Student()
obj2.setValues("prasad",30,85)
obj2.printValues()

