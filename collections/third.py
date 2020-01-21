x=list()
even=list()
limit=int(input("enter the limit"))
for i in range(0,limit):
    val=int(input("enter the value"))
    x.append(val)
print(x)
for val in x:
    if(val%2==0):
        even.append(val)
    else:
        break
print(even)



x=list()
odd=list()
limit=int(input("enter the limit"))
for i in range(0,limit):
    val=int(input("enter the value"))
    x.append(val)
print(x)
for val in x:
    if(val%2!=0):
        odd.append(val)
    else:
        break
print(odd)