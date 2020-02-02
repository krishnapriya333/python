lst=[10,10,20,30,40]
x=set(lst)
print(x)

st1={10,40,50,30}
st2={30,20,40}
un=st1|st2
print(un)
sec=st1&st2
# sec=st1.intersection(st2)
print(sec)
diff=st1.difference(st2)
print(diff)
