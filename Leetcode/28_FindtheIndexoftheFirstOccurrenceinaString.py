# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 
