z=[10,25,40,36,56,78,98,43]
cnt=len(z)
for i in range(0,cnt):
     if(z[i]%2==0):
         print(z[i])
     else:
         pass

z = [10, 25, 40, 36, 56, 78, 98, 43]
cnt=len(z)
for i in range(0,cnt):
    if(z[i]%2!=0):
        print(z[i])
    else:
         pass

z = [10, 25, 40, 36, 56, 78, 98, 43]
cnt=len(z)
for i in range(0,cnt):
   if(z[i]%2==0):
       print(z[i]**2)
   else:
        pass

z = [10, 25, 40, 36, 56, 78, 98, 43]
cnt=len(z)
sum=0
for i in range(0,cnt):
        if(z[i]%2==0):
            sum=sum+(z[i]**2)
        else:
             pass
print("sum=",sum)