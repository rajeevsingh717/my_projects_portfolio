"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        min_len = float('inf')
        curr_sum = 0
        while end < len(nums):
            if curr_sum >= target:
                min_len = min(min_len, end - start)
                curr_sum -= nums[start]
                start += 1
            else:
                curr_sum += nums[end]
                end += 1

        while  curr_sum >= target: ## for edge case when loop ends, we need to shorten from the left side and find the minimum length by keep reducing left side element from curr_sum
            min_len = min(min_len, end - start)
            curr_sum -= nums[start]
            start += 1 
        
    
        return min_len if min_len < float('inf') else 0

     
