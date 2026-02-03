class Solution:
    def isPalindrome(self, x: int) -> bool:
        strr= str(x)
        return strr == strr[::-1]
