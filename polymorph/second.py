#method overreading
class person:
    def setPerson(self, age,name):
        self.age = age
        self.name = name
    def __str__(self):
       return self.name +str(self.age)







ob=person()
ob.setPerson(25,"krishna")
print(ob)