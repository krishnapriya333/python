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
