# line = "hi hello hi how"
# words=line.split(" ")
# print(words)
# dict={}
# for word in words:
#     if(word not in dict):
#         dict[word]=1
#     else:
#         dict[word]+=1
# for item in dict:
#     print(item,end=":")
#     print(dict[item])
# print(dict)



ch= "A B A A B C"
words=ch.split(" ")
dict={}
for val in words :
    if(val not in dict):
        dict[val]=1
    else:
        print("first recursive character=",val)
        break





