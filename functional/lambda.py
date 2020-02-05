f=lambda no:no**2
print(f(5))
f=lambda no1,no2:no1+no2
print(f(5,6))
f=lambda no1,no2:no1/no2
print(f(5,2))
f=lambda no1,no2:no1*no2
print(f(5,2))






lst=[10,11,12,13,14,15,16]




def square(no):
    return no**2
squ=list(map(square,lst))
print(squ)



def even(no):
    return no%2==0
eve=list(filter(even,lst))
print(eve)