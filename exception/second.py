# no1=int(input("enter the value of no1"))
# no2=int(input("enter the value of no2"))
# lst=[10,30,40]
# try:
#     no3=no1/no2
#     print(no3)
#     print("i have one db transaction")
#
# except Exception as e:
#     print(e.args)
#
# try:
#     ind = int(input("enter the index position"))
#     print(lst[ind])
# except Exception as e:
#     print(e.args)



no1=int(input("enter the value of no1"))
no2=int(input("enter the value of no2"))
try:
    no3=no1/no2
    print(no3)
    print("i have one db transaction")
except:
    no2=int(input("enter the value for num2"))
    try:
        no3=no1/no2
        print(no3)
    except Exception as e:
        print(e.args)
finally:
    print("inside finally block")
