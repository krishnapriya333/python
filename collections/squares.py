# x=list()
# even=list()
# square=list()
# limit=int(input("enter the limit"))
# for i in range(0,limit):
#     val=int(input("enter the value"))
#     x.append(val)
# print(x)
# for val in x:
#     if(val%2==0):
#         even.append(val)
#     else:
#         pass
# print(even)
# for val in even:
#     if (val % 2 == 0):
#         square.append(val**2)
#     else:
#         pass
# print(square)


x=list()
even=list()
sum=0
limit=int(input("enter the limit"))
for i in range(0,limit):
    val=int(input("enter the value"))
    x.append(val)
print(x)
for val in x:
    if(val%2==0):
        even.append(val)
    else:
        pass
print(even)
for val in even:
    sum=sum+(val**2)
    continue

print("sum=",sum)
