""" Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        s = s[::-1]
        s = [char for char in s]
        
        start, end = 0, 0
        while end < len(s):
            if s[end] == " ":
                print(start , end-1)
                rev(start, end-1)
                start = end+1
            end += 1
     
        rev(start,len(s)-1)
        s = "".join(s)
        s = " ".join(s.split())
        return s.strip()


        
