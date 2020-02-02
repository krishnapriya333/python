import re
f=open("/home/luminar/python/vehicles","r")
rule='KL[0-9]{2}[A-Z]{2}[0-9]{4}'

for val in f:
    match=re.match(rule,val)
    if(match!=None):
        print(val)
    else:
        pass











# import re
# f=open("/home/luminar/python/vehicles","r")
# rule='KL[0-9]{2}[A-Z]{2}[0-9]{4}'
#
# for val in f:
#     numbers=val.split(",")
#     for num in numbers:
#         match=re.match(rule,num)
#         if(match!=None):
#             print(num)
#         else:
#             pass



