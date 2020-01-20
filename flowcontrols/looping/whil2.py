num=int(input("enter the num"))
#while(num!=0):
    #i=num%10
   # print(i,end="")
   # num=num//10
reverse=0
while(num!=0):
    i=num%10
    reverse=(reverse*10)+i
    num=num//10
print(reverse)

def reverse(num):
    reverse = 0
    while (num != 0):
        i = num % 10
        reverse = (reverse * 10) + i
        num = num // 10
    if((num//10)==0):
        res=reverse
        return res
x=reverse(123)
print(x)





