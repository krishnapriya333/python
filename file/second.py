f=open("/home/luminar/python/abc")

for val in f:
    numbers=val.split(",")
    for num in numbers:
        print(num)