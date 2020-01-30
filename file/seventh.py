f1=open("/home/luminar/python/students","r")
f2=open("/home/luminar/python/pass","r")
f3=open("fail.txt","w")
x=set()
y=set()

for data in f1:
    x.add(data.rstrip("\n"))
print(x)
for data in f2:
    y.add(data.rstrip("\n"))
print(y)

diff=x.difference(y)
z=diff
for i in z:
    f3.write(str(i))
    f3.write("\n")