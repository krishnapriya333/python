i=10
while(i>0):
    print(i)
    i=i-1

#TO PRINT FACTORIAL OF A NUMBER
num=int(input("enter the num"))
i=1
res=1
while(i<=num):
    res=res*num
    num=num-1
print(res)



def fact(num):
    i = 1
    res = 1
    while (i <= num):
        res = res * num
        num = num -1
    if(num==0):
         val=res
         return val
x=fact(3)
print(x)





