def largestOddNumber(num: str):

    ptr = len(num)-1
    for i in range(len(num)):
        n = int(num[ptr])
        if(n^1 != n+1): #can be written as (n%2==0)

            return num[:len(num)-i]
        ptr-=1
    return ''
            
print(largestOddNumber('35427'))