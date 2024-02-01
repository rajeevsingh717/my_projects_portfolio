""" You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1. 
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1 = m-1
        r2 = n-1
        index = m+n-1
        while r1>=0 and r2>=0:
            if nums1[r1] > nums2[r2]:
                nums1[index] = nums1[r1]
                r1 -= 1
            else:
                nums1[index] = nums2[r2]
                r2 -= 1
            
            index -= 1
        
        while r2>= 0:
            nums1[index] = nums2[r2]
            index -= 1
            r2 -= 1

        print(nums1)


        
