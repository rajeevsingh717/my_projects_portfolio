# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int: 
        max_area = curr_area =  0
        l = 0
        r = len(height) - 1
        while l < r:
            width = r-l
            curr_area = width * min(height[l], height[r])
            print(curr_area)
            max_area = max(curr_area,max_area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        
        return max_area

        



        
