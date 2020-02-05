lst1=[1,2,3]
lst2=[4,5,6]
# for i in lst1:
#     for j in lst2:
#         print((i,j))

lst=[(item1,item2) for item1 in lst1 for item2 in lst2]
print(lst)

lst=[item1+item2 for item1 in lst1 for item2 in lst2 ]
print(lst)