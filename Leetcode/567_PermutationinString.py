"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = Counter(s1) ## creating dictionary of S1 chars
        
        w = len(s1) ## length of S1 Chars

        for i in range(0, len(s2)): 
            if s2[i] in s1map:
                s1map[s2[i]] -= 1
            
            ##Following condition checks if we have processed at least w characters in s2 (the length of s1) and if the character that was at the beginning of the sliding window (i.e., s2[i-w]) is present in the cntr dictionary. If both conditions are met, it increases the count of s2[i-w] in the cntr dictionary by 1. This effectively moves the sliding window one character to the right.
            if i >= w and s2[i-w] in s1map:
                s1map[s2[i-w]] += 1

            ## checking if each key is 0 in the dictionary
            if all(s1map[i] == 0 for i in s1map):
                return True
        
        return False
            
            

     
