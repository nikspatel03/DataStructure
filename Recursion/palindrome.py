"""

To check given string is palindrome or not using recursion.

"""


def isPalindrome(myStr):
    if len(myStr) < 1:
        return True
    else:
        return False if myStr[0] != myStr[-1] else isPalindrome(myStr[1:-1])

print(isPalindrome("aba"))
print(isPalindrome("wassamassaw"))
print(isPalindrome("hello"))
