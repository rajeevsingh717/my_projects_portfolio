# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxstr=''
        for i in range(0,len(s)):
            ## odd string palindrome
            l=i
            r=i 
            while l>=0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                l -= 1
                r += 1
            
            if len(curr) > len(maxstr):
                maxstr = curr
            ## even palindrome
            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                l -= 1
                r += 1
            
            if len(curr) > len(maxstr):
                maxstr = curr
            
        return maxstr





