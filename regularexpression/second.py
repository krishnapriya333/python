import re
# x='\w' #except special charcters and space
# x='[abc]'  #find a,b and c
# x='[^abc]' #find except a,b and c
x='[^a-z]' #find a to z letters
# x='[A-Z]'#find uppercase letters
# x='[a-zA-Z]' #find lowercase and uppercase
# x='[a-zA-Z0-9]'#find lc ,uc and numbers
# x='\s'  #find space
# x='\d'  #find no's
# x='\D'  #except digits
# x='\W' #special character and space


matcher=re.finditer(x,'a7b @ak9z')
for match in matcher:
    print("match available at", match.start())
    print("match=", match.group())