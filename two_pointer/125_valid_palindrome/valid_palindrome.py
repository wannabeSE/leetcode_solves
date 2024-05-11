import re

def isPalindrome(s: str):
    
    cleaned_text = re.sub(r'[^a-zA-Z0-9]','', s)
    lowerCased = cleaned_text.lower()
    left, right  = 0, len(lowerCased) - 1

    if(cleaned_text == ''):
        return True
    for i in range(len(lowerCased)):
        if left != right and left < right:
            if lowerCased[left] == lowerCased[right]:
                left , right= left + 1 , right - 1

            else:
                return False

        else:
            return True
print(isPalindrome('abba'))
