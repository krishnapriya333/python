lst=[3,5,4,8,1,9,2,7,6]
lst.sort()
print(lst)
val=int(input("enter the value"))
ll=0
ul=len(lst)-1
res=lst[ll]+lst[ul]
while(ll<ul):
    res = lst[ll] + lst[ul]
    if(res<val):
        ll+=1
    elif(val<res):
        ul-=1
    elif(val==res):
        print(lst[ll], lst[ul])
        ll=ll+1




