"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            
            mid = (l+r)//2
            
            if nums[mid] > nums[r]: ## check with the right most element if greater than answer is second half
                l = mid + 1 ## moving towards the second half
            else:
                r = mid ## moving towards the 1st half
        
        return nums[l]
    
    """Note to self - 
    1) while changing the left and right pointer if I am not ignoring the middle element then run the loop until l<r . 
    2) In Binary problems where there is no target given we have to make sure to iterate through all the elements therefor not ignoring the middle element. Many times the middle element is the one we want and as soon as the left and right index matches, the program has to exit.
    3) In Binary problems where there is target given, then typically we compare the mid elelemt with the target and that is why we ignore that element in the next iteration"""
                
            
