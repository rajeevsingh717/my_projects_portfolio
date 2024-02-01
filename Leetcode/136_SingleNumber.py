"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:

Input: nums = [2,2,1]
Output: 1
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ls=[]
        for i in nums:
            if i in ls:
                ls.remove(i)
            else:
                ls.append(i)
        return ls[0]
