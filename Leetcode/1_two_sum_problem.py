""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lsd = {}
        for i in range(0,len(nums)):
            if target - nums[i] in lsd:
                return [lsd[target - nums[i]],i]
            else:
                lsd[nums[i]] = i
                
        return []
