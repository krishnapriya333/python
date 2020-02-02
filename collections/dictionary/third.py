line = "hi hello hi how are you i am fine"
words=line.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

tmp=list()
for k,v in dict.items():
    tmp.append((v,k))
tmp=sorted(tmp,reverse=True)
print(tmp[0][1])