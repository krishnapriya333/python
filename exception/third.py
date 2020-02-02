
try:
    f = open("ml.txt")
    for data in f:
        print(data)
except Exception as e:
    print(e.args)
    