lst=[3,5,6,4,7,9,8,1,2]
lst.sort()
print(lst)
element=int(input("enter the value"))
flag=0
ll=0
ul=len(lst)
print(ul)
mid=(ll+ul)//2
while(ll<ul):
    if(element<lst[mid]):
        ul=mid-1
    elif(element>lst[mid]):
        ll=mid+1
    else:
        flag+=1
        break
    mid=(ll+ul)//2
    if(ll>=ul):
        break
if(flag==1):
    print("element found")
else:
    print("element not found")





