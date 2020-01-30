#function overloading and method overloading
def add(no1):
    no2=20
    print(no1+no2)


def add(no1,no2,no3):
   res=no1+no2
   print(res)


def add(no1,no2,no3,no4):
    res = no1+no2+no3+no4
    print(res)

add(20)
add(20,30,40)
add(20,30,40,50)#only work recently implemented method


