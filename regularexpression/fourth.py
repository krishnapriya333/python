import re
var=input("enter the variable")
rule='[a-k][3 6 9][a-zA-Z0-9]*'
match=re.fullmatch(rule,var)
if(match!=None):
        print("valid")
else:
        print("invalid")
