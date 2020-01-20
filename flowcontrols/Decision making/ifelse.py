no1=int(input("enter value for no1"))
if(no1>0):
        print(no1," is positive")
else:
        print(no1, "is negative")



no1=int(input("enter value for no1"))
no2=int(input("enter value for no2"))

if(no1>no2):
        print(no1, "is greater than ",no2)
elif(no1<no2):
         print(no2, "is greater than", no1)
else:
        print("both numbers are equal")



def greater(no1,no2):
        if (no1 > no2):
               res=no1
               return res
        elif (no1 < no2):
                res=no2
                return res
        else:
                res="both numbers are equal "
                return res
x=greater(2,15)
print(x)