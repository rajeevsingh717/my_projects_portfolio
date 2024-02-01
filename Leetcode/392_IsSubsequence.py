"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        t_left = 0
        s_left = 0
        while t_left < len(t): ## check until the end of target string
            if s_left < len(s) and t[t_left] == s[s_left]: ## check if the source string length is within limit
                s_left += 1 ## increate the source string left index only if the match found
            t_left += 1

        return s_left == len(s)
