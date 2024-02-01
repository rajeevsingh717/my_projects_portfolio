"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        freq = [[] for i in range(len(nums)+1)]
        print(freq)

        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        
      
        for value, key in nums_dict.items():
            print(value, key)
            freq[key].append(value)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if  len(res) == k:
                    return res

                    
