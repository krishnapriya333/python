no1=int(input("enter value for num1"))
no2=int(input("enter value for num2"))
no3=int(input("enter value for num3"))
if(no1>no2):
        if(no1>no3):
            print("max=no1")
        else:
            print("max=no3")
else:
        if(no2>no3):
            print("max=no2")
        else:
            print("max=no3")

if((no1>no2)&(no1>no3)):
        print("max=no1")
elif((no2>no1)&(no2>no3)):
        print("max=no2")
elif((no3>no1)&(no3>no2)):
        print("max=no3")
else:
        print("no1=no2=no3")