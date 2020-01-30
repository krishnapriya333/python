class person:
    def __init__(self, age, name, sal):
        self.age = age
        self.name = name
        self.sal = sal
    #
    # def printPerson(self):
    #     print("age=", self.age)
    #     print("name=", self.name)

    def __str__(self):
        return self.name


f = open("/home/luminar/python/ab")
lst = []

for data in f:
    persons = data.rstrip("\n").split(",")
    age = persons[0]
    name = persons[1]
    sal = persons[2]
    if(int(sal)>=25000):
        ob = person(age,name,sal)
        print(ob)
        lst.append(ob)

    else:
        pass

print("the no of person with salary greater than 25000=",len(lst))

















