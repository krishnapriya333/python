#LIST COMPREHENSION
lst=[10,20,30,40,13,25]

values=[item**2 for item in lst]
print(values)


y=[item for item in lst if item%2==0]
print(y)