"""
Given a string s and an integer k, return the length of the longest 
substring
 of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
"""

class Solution:
    ## sliding window - using dictionary to keep the char count within each substring
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_count = {}
        l = 0
        max_len = 0
    
        for r in range(len(s)):
            # Update the count of the character at the right end of the window
            char_count[s[r]] = char_count.get(s[r],0) + 1
            
            # If the window has more than k distinct characters, shrink it from the left
            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len

        
