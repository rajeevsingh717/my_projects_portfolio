"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 """
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums

        n = len(nums)
        res = []
        max_deque = deque()

        for i in range(n):
            # Remove elements outside the current window
            while max_deque and max_deque[0] < i - k + 1:
                max_deque.popleft()

            # Remove elements in the deque that are smaller than the current element
            while max_deque and nums[i] > nums[max_deque[-1]]:
                max_deque.pop()

            max_deque.append(i)

            if i >= k - 1:
                res.append(nums[max_deque[0]])

        return res
