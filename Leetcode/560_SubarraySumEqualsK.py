"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1} ## Dictionary element for when the curr_sum - target = 0
        ans = 0
        target = k
        curr_sum = 0
        for item in nums:
            curr_sum += item
            if curr_sum-target in d:
                ans += d[curr_sum-target]
            if curr_sum in d:
                d[curr_sum] += 1
            else:
                d[curr_sum] = 1
        
        return  ans
