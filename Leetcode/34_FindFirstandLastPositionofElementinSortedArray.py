# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0 , len(nums) - 1
            result = -1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    result = mid
            
            return result

        def find_last(nums, target):
            left, right = 0 , len(nums) - 1
            result = -1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    result = mid
            
            return result

        first = find_first(nums, target)
        last = find_last(nums, target)

        return [first,last]



        
        
