# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum > target:
                    right -= 1
                else:
                    left += 1
                
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                
        return res


