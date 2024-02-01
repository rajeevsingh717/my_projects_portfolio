"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        z = [0]*26
        for i in range(0,len(s)):
            z[ord(s[i]) - ord('a')] += 1
            z[ord(t[i]) - ord('a')] -= 1
        print(z)

        for i in z:
            if i >0:
                return False
        return True

