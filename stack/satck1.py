stk=[]
limit=int(input("enter the limit"))
choice=int(input("1 for push,2 for display,3 for pop"))
top=0
while(top<limit):
    for i in range(0,limit):
        item = int(input("enter the item"))
        if(choice==1):
            stk.append(item)
            top+=1
        elif(choice==2):
            stk.push(item)
            top+=1
        else:
            stk.pop()
            top+=1
print(stk)










