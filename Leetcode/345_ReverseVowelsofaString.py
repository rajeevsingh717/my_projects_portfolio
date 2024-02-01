"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:

Input: s = "hello"
Output: "holle"
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] in vowel and s[r] in vowel:
                s[l] , s[r] = s[r], s[l]
                l += 1 
                r -= 1
            if s[l] not in vowel:
                l += 1
            if s[r] not in vowel:
                r -= 1 

        return "".join(s)



