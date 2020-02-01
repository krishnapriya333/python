#quantifiers

import re
# x='a+' #count a
# x='a*' #count a and others as space
# x='a?'   #find a and others as space
#x='a{2}' # min count of a is 2
# x='a{2,3}' #min 2 max 3
# x='^a' # to check starting with a
# x='a$' # to check ending with a
matcher=re.finditer(x,'abaabaaabacaab')
for match in matcher:
    print("match available at", match.start())
    print("match=", match.group())