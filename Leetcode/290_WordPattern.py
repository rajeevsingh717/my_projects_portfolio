"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split(" "))
        if len(pattern) != len(s) or len(set(pattern))!=len(set(s)): ## edge case - if the length does not match or number of unique word and char(from pattern) does not match
            return False
        pat_dict = {k:'' for k in pattern} ## created a dictionary with pattern to hold the words from "s"
        for i in range(0,len(pattern)):
            if pat_dict[pattern[i]] == '': ## if the correcponding value is empty in dictionary then set the word
                pat_dict[pattern[i]] = s[i]
            elif pat_dict[pattern[i]] != s[i]: ## if the correcponding value is not empty then check if its matching with corresponding word or not. If not return false
                return False
        return True
