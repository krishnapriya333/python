def secondlargest(no1, no2, no3):
    if ((no2 < no1<no3)):
        res = no1
        return res
    elif ((no1 < no2<no3)):
        res = no2
        return res
    elif ((no1 < no3<no2)):
        res = no3
        return res
    elif ((no2 < no3 < no1)):
        res = no3
        return res
    elif ((no3 < no1 < no2)):
        res = no1
        return res
    elif ((no3 < no2 < no1)):
        res = no3
        return res
    else:
        res = "numbers are equal"
        return res


x = secondlargest(40,56,76)

print(x)