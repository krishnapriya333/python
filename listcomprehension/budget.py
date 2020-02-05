
class student:
    def __init__(self,date,purpose,expence):
        self.date=date
        self.purpose=purpose
        self.expence=expence
    def __str__(self):
        return self.date

    def __str__(self):
        return self.purpose

    def __str__(self):
        return self.expence

lst=[]
try:
    f=open("/home/luminar/python/listcomprehension/dataset")
    for data in f:
        values=data.rstrip("\n").split(',')
        print(values)
        date=values[0]
        purpose=values[1]
        expence=values[2]
        ob=student(date,purpose,expence)
        lst.append(ob)

except Exception as e:
    print(e.args)


# for item in lst:
#     print(item)

sum=0
a=[int(ob.expence) for ob in lst if ob.date=="01/2/2020"]
print(a)
for val in a:
    sum=sum+val
    continue
print("total expenditure on 01/2/2020 =",sum)

maximum=max(int(ob.expence) for ob in lst  if ob.date=="01/2/2020")
print(maximum)

b=[ob.purpose for ob in lst if ob.date=="01/2/2020" and int(ob.expence)==maximum ]
for item in b:
    print("the max expence on 01/02/2020 in",item)




sum=0
c=[int(ob.expence) for ob in lst if"01/2/2020"<=ob.date<="07/2/2020"]
print(c)
for val in c:
    sum=sum+val
print("total expenditure in first week=",sum)


maximum=max(int(ob.expence) for ob in lst if("01/2/2020"<=ob.date<="07/2/2020"))
print(maximum)


d=[ob.purpose for ob in lst if("01/2/2020"<=ob.date<="07/2/2020") and int(ob.expence)==maximum ]
for item in d:
    print("the max expence on first week in",item)


sum=0
e=[int(ob.expence) for ob in lst if"01/2/2020"<=ob.date<="30/2/2020"]
print(e)
for val in e:
    sum=sum+val
print("total expenditure in a month=",sum)


maximum=max(int(ob.expence) for ob in lst if("01/2/2020"<=ob.date<="30/2/2020"))
print(maximum)


f=[ob.purpose for ob in lst if("01/2/2020"<=ob.date<="30/2/2020") and int(ob.expence)==maximum ]
for item in f:
    print("the max expence in a month is in",item)

