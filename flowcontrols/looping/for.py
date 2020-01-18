#for i in range(0,10):
#    print(i)

#for i in range(0,10,2):
   # print(i)
#for i in range(1,10,2):
 #   print(i)
no1=int(input("enter lower limit"))
no2=int(input("enter upper limit"))
if((no1%2==0)&(no2%2==0)):
    for i in range(no1,no2,2):
        print(i)
elif((no1%2==0)&(no2%2!=0)):
    for i in range(no1,no2,2):
        print(i)
elif((no1%2!=0)&(no2%2==0)):
    for i in range(no1+1,no2,2):
        print(i)
else:
    for i in range(no1+1,no2+1,2):
        print(i)







