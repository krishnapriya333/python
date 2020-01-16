for i in range(0,3):
   for j in range(0,3):
        print(i,end="")
   print()
for i in range(0,3):
    for j in range(0,3):
        print(j,end="")
    print()
for i in range(0,3):
    for j in range(0,i+1):
        print("*",end="\t")
    print()