def fibonacci(n):
    n1=0
    n2=1
    count=0
    while(count<=n):
            print(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1

fibonacci(5)

