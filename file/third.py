f=open("/home/luminar/python/abc")
lst=list()
dict={}
for word in f:
    words=word.rstrip("\n").split(" ")
#     for num in words:
#       lst.append(num.rstrip("\n"))
# print(lst)
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)






