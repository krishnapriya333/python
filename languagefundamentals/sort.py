no1=int(input("enter value for num1"))
no2=int(input("enter value for num2"))
no3=int(input("enter value for num3"))
def sort():
    a=min(no1,no2,no3)
    b=max(no1,no2,no3)
    c=(no1+no2+no3)-a-b
    print(a,b,c)
sort()

