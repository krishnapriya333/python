lst=[20,13,14,15,27,28]
f1=open("odd.txt","w")
f2=open("even.txt","w")
for item in lst:
    if(item%2==0):
        f1.write(str(item))
        f1.write("\n")
    else:
        f2.write(str(item))
        f2.write("\n")
        