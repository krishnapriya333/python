ch= "A B A A B C"
words=ch.split(" ")
dict={}
for val in words :
    if(val not in dict):
        dict[val]=1
    else:

