no1=int(input("enter the value of no1"))
no2=int(input("enter the value of no2"))
try:
    no3=no1/no2
    print(no3)
    print("i have one db transaction")
except:
    print("exception occured")








lst=[10,20,30]
try:
    ind=int(input("enter the index position"))
    print(lst[ind])
except:
    print("enter another index position")