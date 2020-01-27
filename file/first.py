# f=open("/home/luminar/python/abc",'r')
# print(f.mode)
# for data in f:
#     print(data)

f=open("/home/luminar/python/abc")
lst=list()
for val in f:
    if(int(val)%2==0):
        print(val)
        lst.append(val.rstrip("\n"))
    else:
        pass

print(lst)