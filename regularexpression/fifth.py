import re
f=open("/home/luminar/python/vehicles","r")
f2=open("vehicles.txt","w")
rule='KL[0-9]{2}[A-Z]{2}[0-9]{4}'

for val in f:
    val=val.rstrip("\n")
    match=re.fullmatch(rule,val)
    if(match!=None):
        f2.write(val)
        f2.write("\n")
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



