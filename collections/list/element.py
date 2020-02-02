#CHECK AN ELEMENT IN A LIST
lst=[10,20,21,22,23]
flag=0
element=int(input("enter element for search"))
for item in lst:
    if(item==element):
        flag+=1
        break
    else:
        flag=0
if(flag==0):
    print("no element found")
else:
    print("element found")
