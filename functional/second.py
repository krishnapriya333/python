class student:
    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
    def __str__(self):
        return self.name
    #
    # def __str__(self):
    #     return self.id
    #
    # def __str__(self):
    #     return self.total

lst=[]
try:
    f=open("/home/luminar/python/student")
    for data in f:
        values=data.rstrip("\n").split(',')
        print(values)
        id=values[0]
        name=values[1]
        total=values[2]
        ob=student(id,name,total)
        lst.append(ob)

except Exception as e:
    print(e.args)

for item in lst:
    print(item)

upper=list(map(lambda ob:ob.name.upper(),lst))
print(upper)

names=list(filter(lambda ob:ob.name[0]=='a',lst))
for name in names:
    print("names=",name)

z=list(filter(lambda ob:int(ob.total)>160,lst))
for item in z:
    print(item)


maximum=max((ob.total,ob.name,ob.id) for ob in lst)
print(maximum)

maximum=max(ob.total for ob in lst)
y=[(ob.id,ob.name,ob.total) for ob in lst if ob.total==maximum]
print(y)






