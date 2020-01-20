no1=int(input("enter value for num1"))
no2=int(input("enter value for num2"))
no3=int(input("enter value for num3"))
if(no1>no2):
        if(no1>no3):
            print("max=",no1)
        else:
            print("max=",no3)
elif(no1<no2):
        if(no2>no3):
            print("max=",no2)
        else:
            print("max=",no3)
else:
        print("numbers are equal")


def max(no1,no2,no3):
    if((no1>no2)&(no1>no3)):
        res=max=no1
        return res
    elif((no2>no1)&(no2>no3)):
        res=max=no2
        return res
    elif((no3>no1)&(no3>no2)):
        res=max=no3
        return res
    else:
        res="3 numbers are equal"
        return res

x=max(23,67,45)
print(x)