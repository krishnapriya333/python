f=open("/home/luminar/python/abc2")
f1=open("movies.txt","w")
lst=list()
dict={}
for word in f:
    words=word.split(",")
    lst.append(words)
print(lst)
for word in lst:
    if(word[2] not in dict):
        dict[word[2]]=1
    else:
        dict[word[2]]+=1
print(dict)
tmp=list()
for k,v in dict.items():
    tmp.append((k,v))
tmp=sorted(tmp)
print(tmp)
for data in tmp:
    print(data)
    f1.write(str(data))
    f1.write("\n")