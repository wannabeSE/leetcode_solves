class Solution:
    def encode(self, strs:list) -> str:
        encodedString = ''
        for i, ele in enumerate(strs):
            for s in ele:
                if(ord(s) < 255):
                    encodedChar = ord(s) + 1
                else:
                    encodedChar = ord(s) - 1
                encodedString+=chr(encodedChar)
            encodedString+='0'
        #print(encodedString)
        return encodedString
    def decode(self, s:str) -> list[str]:
        res = []
        decodedString = ''
        for i in s:
            if(i == '0'):
                res.append(decodedString)
                decodedString = ''
                continue
            elif(ord(i) < 255):
                decodedChar = ord(i) - 1 
            else:
                decodedChar = ord(i) + 1
            decodedString += chr(decodedChar)
        return res
                
s = Solution()
encoded = s.encode(["neet","code","love","you"])
print(encoded)
print(s.decode(encoded))