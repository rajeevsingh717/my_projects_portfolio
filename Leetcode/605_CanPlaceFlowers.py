"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n==0: return True ## if there no flowers
        
        if len(flowerbed)==1: ## if flowerbed is of only 1 element
            if flowerbed[0]==0:
                return True
            else:
                return False
        
        for i in range(0,len(flowerbed)):
            if i == 0: ## when 1st place is elligble
                if flowerbed[i]==0 and flowerbed[i+1]!=1:
                    flowerbed[i] = 1
                    n -= 1
            if i == len(flowerbed) - 1: ## when last place is elligble
                if flowerbed[i] == 0 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            if flowerbed[i] == 1:
                continue
            else: ## when elligible places are inbetween first and last place
                if  flowerbed[i-1] != 1 and flowerbed[i+1]!=1:
                    flowerbed[i] = 1
                    n -= 1
            if n==0: ## if there are "n" places elligble to fit n-1 flower and we run out of flower.
                return True
        
        return n==0 ## if all "n" elligble places filled with "n" flowers

            
        

                
