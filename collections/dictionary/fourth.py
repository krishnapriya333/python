ch= "C B A C A B D A"
words=ch.split(" ")
dict={}
for val in words :
    if(val not in dict):
        dict[val]=1
    else:
        dict[val]+=1
print(dict)
tmp=list()
for k,v in dict.items():
    tmp.append((v,k))
tmp=sorted(tmp)
print(tmp)
print(tmp[0][1])