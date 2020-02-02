lst=[-2,3,0,-1,1]
lst.sort()
print(lst)
ll=0
ul=len(lst)-1
flag=0
while(ll<ul):
   for i in range(ll,ul):
        if(lst[i]<0):
            pass
        elif(lst[i]==0):
            if(lst[i+1]!=1):
                print("least positive missing integer=",1)
        else:#(lst[i]>0)
            if (lst[i+1]!=2):
                flag=0
            ll+=1
        if(ll==ul):
            break
if(flag==0):
    print("least positive missing integer=", i-1)




