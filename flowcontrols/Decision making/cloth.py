clothtype=int(input("enter the clothtype 1 for cotton 2 for silk 3 for linen"))
amount=int(input("enter the payamnt"))

if(clothtype==1):
        if(amount>20000):
                print(amount*(10/100))
        elif(15000<amount<=20000):
                print(amount*(9/100))
        elif(14000<amount<=15000):
                print(amount*(7/100))
        elif(amount<14000):
                print(amount*(2/100))
        else:
                print("none")
else:
        if(clothtype==2):
                if (amount > 20000):
                         print(amount*(15/100))
                elif (15000 < amount <= 20000):
                        print(amount*(15/100))
                elif (14000 < amount <= 15000):
                         print(amount*(9/100))
                elif (amount < 14000):
                         print(amount*(5/100))
                else:
                        print("none")
        else:
                if (clothtype == 3):
                        if (amount > 20000):
                                    print(amount*(15/100))
                        elif (15000 < amount <= 20000):
                                 print(amount*(10/100))
                        elif (14000 < amount <= 15000):
                                  print(amount*(9/100))
                        elif (amount < 14000):
                                print(amount*(5/100))
                        else:
                                print("none")
                else:
                        print("not type of cloth")




