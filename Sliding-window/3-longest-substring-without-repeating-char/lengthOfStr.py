def lengthOgLongestSubstring(s) -> int:
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l]) #? removing the repeating character
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1) #? r - l + 1 = window size
    return res
print(lengthOgLongestSubstring('au'))