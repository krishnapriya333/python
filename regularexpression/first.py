import re
count=0
matcher=re.finditer('ab','babaabab')
for match in matcher:
    print("match available at",match.start())
    print("match=",match.group())
    count+=1
print("count=",count)

