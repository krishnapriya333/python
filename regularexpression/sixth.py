import re
var=input("enter the mail id")
rule='\w[a-zA-Z0-9_]*@gmail.com'
match=re.fullmatch(rule,var)
if(match!=None):
    print("valid")
else:
    print("invalid")