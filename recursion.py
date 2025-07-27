### Palindrome

def palindrome(s):
    if len(s) == 0:
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])