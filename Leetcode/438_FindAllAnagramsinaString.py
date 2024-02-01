"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    ## solving using sliding window technique
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = {}
        for i in range(0,len(p)):
            pdict[p[i]] = pdict.get(p[i],0) + 1
        
        plength = len(p)
        res = []
        for i in range(0,len(s)):
            if s[i] in pdict: ## comparing against dictionary, decrese the value if found
                pdict[s[i]] -= 1
            if i >= plength and s[i-plength] in pdict: ## if the left most value going out of window and it is part of dictionary then set the value back to 1 to compare against the next window
                pdict[s[i-plength]] += 1
            if all (pdict[val] == 0 for val in pdict): ## if at point of time all values are 0 then that's one of th answer
                res.append(i-plength+1) ## saving the anagram starting point in res
        
        return res




        
