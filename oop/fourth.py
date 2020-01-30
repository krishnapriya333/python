class parent:
    def phonee(self):
        print("i have nokia 1100")
class child(parent):
    def phone(self):
        print("i have i phone")




c=child()
c.phone()
c.phonee()

p=parent()
p.phonee()

# student is person relationship
class person:
    def setPerson(self,age,name):
        self.age=age
        self.name=name
    def printPerson(self):
        print("age=",self.age)
        print("name=",self.name)
class student(person):
    def setStudent(self,rol,course):
        self.rol=rol
        self.course=course
    def printDetails(self):
        print("rol=",self.rol)
        print("course=",self.course)

ob=student()
ob.setPerson(25,"krishna")
ob.setStudent(12,"mca")
ob.printPerson()
ob.printDetails()