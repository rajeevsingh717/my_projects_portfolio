"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first: ## if any number is smaller than first then change the first to n
                first = n 
            elif n <= second: ## if any number is smaller than second then change the second to n
                second = n
            else: ## if above 2 if condition did met then it means 3rd number is definietly greater than 1st two, so return False
                return True
        return False
        
