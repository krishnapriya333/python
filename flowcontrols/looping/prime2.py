# SUM OF PRIME NO'S IN A RANGE
no1=int(input("enter the lower limit"))
no2=int(input("enter the value upper limit"))
sum=0
for num in range(no1,no2+1):
    flag=0
    for i in range(2,num):
        if(num % i==0):
            flag=flag+1
            break
    if(flag==0):
        sum=sum+num
    else:
        pass


print("sum=",sum)




#PRINT PRIME NUMBERS IN A RANGE


no1=int(input("enter the lower limit"))
no2=int(input("enter the value upper limit"))
for num in range(no1,no2+1):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
            break
    if(flag==0):
        print(num)
    else:
        pass

