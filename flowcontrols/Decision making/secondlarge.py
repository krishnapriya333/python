no1=int(input("enter value for num1"))
no2=int(input("enter value for num2"))
no3=int(input("enter value for num3"))
if((no2<no1)&(no1<no3)):
        print(no1,"is second largest")
elif((no1<no2)&(no2<no3)):
        print(no2,"is second largest")
elif((no1<no3)&(no3<no2)):
        print(no3,"is second largest")
else:
        print("no1=no2=no3")
