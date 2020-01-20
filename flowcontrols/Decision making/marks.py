



def grade(m1,m2,m3):
        m=m1+m2+m3
        if(m>145):
                res="grade is A+"
                return res
        elif(140<m<=145):
                res="grade is A"
                return res
        elif(135<m<=140):
                 res="grade is B+"
                 return res
        elif(130<=m<=135):
                res="grade is B"
                return res
        else:
                res="failed"
                return res
x=grade(45,43,56)
print(x)