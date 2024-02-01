"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        s = e = 0
        res = []
        while e < len(nums):
           if e+1 < len(nums) and nums[e+1] - nums[e] > 1  : ## check from next number to current number if gap is more than 1
               st = str(nums[s]) + "->" + str(nums[e]) if nums[s] != nums[e] else str(nums[s]) 
               res.append(st)
               s = e+1
           e = e+1
        
        
        st = str(nums[s]) + "->" + str(nums[e-1]) if nums[s] != nums[e-1] else str(nums[s]) 
        
        res.append(st)              
        return res
