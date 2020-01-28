f=open("/home/luminar/python/abc1")
lst=list()
dict={}
for word in f:
    words=word.split(",")
    lst.append(words)
print(lst)
for word in lst:
        if(word[2] not in dict):
            dict[word[2]] = 1
        else:
            dict[word[2]]+=1
print(dict)
tmp=list()
for k,v in dict.items():
    tmp.append((v,k))
tmp=sorted(tmp,reverse=True)
print(tmp)
print("the age is most=",tmp[0][1])
print("the age is least=",tmp[-1][1])
