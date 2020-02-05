import re
num=input("enter the mobile number")
rule='\d{10}'
match=re.fullmatch(rule,num)
if(match!=None):
    print("valid")
else:
    print("invalid")