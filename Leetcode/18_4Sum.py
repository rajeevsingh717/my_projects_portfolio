# 18. 4Sum
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
    
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for the second number
                    continue
                lo = j + 1
                hi = n - 1
            
            while (lo < hi):
                curr_sum = nums[i]+ nums[j] + nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                    
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                    
                else:
                    
                    result.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
    
        return result
