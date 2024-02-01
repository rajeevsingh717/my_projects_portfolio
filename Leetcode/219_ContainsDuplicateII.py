"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0: return False ## if the number to find is 0
        numset = set()  ## creating a set variable to keep the number
        for r in range(len(nums)):
            if nums[r] in numset: ## if found in numset return true
                return True
            numset.add(nums[r]) ## add the number in set if condition not satisfied so far
            if len(numset) == k+1: 
                numset.remove(nums[r-k]) ## as the total number of element in set goes over k remove the element from the left end
            
        return False
