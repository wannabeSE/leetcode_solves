num =3999

roman = [['I',1],['IV',4],['V',5],['IX',9], ['X',10], ['XL',40],['L',50], ['XC',90],['C',100], ['CD',400],['D',500], ['CM',900],['M',1000]]
res=''
for sym, val in reversed(roman): #is able to access the pair as it has two variables
    if num//val:
        count = num//val
        res += (sym*count) #multiplying symbol with number of times it occurred
        num=num%val
print(res)
