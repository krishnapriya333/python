no=int(input("enter the number"))
flag=0
for i in range (2,no):
    if(no%i==0):
        flag=flag+1
        break
    else:
        flag=0
if(flag==0):
    print("it's a prime number")
else:
    print("not a prime number")


