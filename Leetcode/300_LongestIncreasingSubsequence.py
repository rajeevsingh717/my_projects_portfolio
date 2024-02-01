"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
## solving using DP with bottom up approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums) ## every index is initialized with 1

        for i in range(len(nums)-1, -1, -1): ## botom up approach, startin from end
            for j in range(i+1, len(nums)): ## starting from the current index, need to check every element after it, if after element is greater then only update the current index value
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis) ## return the max val
