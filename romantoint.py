symbolValues = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = 'LVIII'
result=0

length = len(s)

for i in range(length):
    temp = symbolValues[s[i]]
    if(i<length-1 and temp< symbolValues[s[i+1]]):
        
        result = result-temp
    else:
        result=result + temp
print(result)