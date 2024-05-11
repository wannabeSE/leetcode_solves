def isAnagram(s:str, t:str):
    dictS={}
    dictT= {}
    flag:bool = False
    if(len(s) != len(t)):
        return flag
    
    for i in range(len(s)):
        if s[i] not in dictS:
            dictS[s[i]] = 1
        else:
            temp = dictS[s[i]]
            temp+=1
            dictS[s[i]] = temp
    for i in range(len(t)):
        if t[i] not in dictT:
            dictT[t[i]] = 1
        else:
            temp = dictT[t[i]]
            temp+=1
            dictT[t[i]] = temp

    for i in dictS:
        if i not in dictT:
            return False
        else:
            if(dictS[i] == dictT[i]):
                flag = True
            else:
                return False
    return flag

            

print(isAnagram('anagram', 'nagaram'))