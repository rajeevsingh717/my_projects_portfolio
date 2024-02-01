"""
Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.
Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len=0
        left=0
        dic={}
        for right in range(len(s)):
            if s[right] not in dic:
                dic[s[right]] = 1
                while len(dic) > 2:
                    dic[s[left]] -= 1
                    if dic[s[left]]==0:
                        del(dic[s[left]])
                    left += 1

            else:
                dic[s[right]] += 1
            max_len = max(max_len,right-left+1)
        return max_len


