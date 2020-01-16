no1=int(input("enter the lower limit"))
no2=int(input("enter the value upper limit"))
sum=0
for num in range(no1,no2+1):
    for i in range(2,num):
        if(num % i==0):
            break
    else:
         print(num)






