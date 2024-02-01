# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        return st==st[::-1]
