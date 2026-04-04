
s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    filtered = ''.join([char.lower() for char in s if char.isalnum()])
    left = 0
    right = len(filtered) - 1
    pal = True
    while left < right:
        if filtered[left] == filtered[right]:
            left +=1
            right -=1
        else:
            pal = False
            break
    return pal




isPalindrome(s)
