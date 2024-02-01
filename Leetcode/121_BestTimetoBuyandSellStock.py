"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_p=0
        while  r <len(prices):
            
            p=prices[r]-prices[l]
            if prices[r] > prices[l]:
                if max_p < p:
                    max_p=p
            else:
                l=r
            r +=1
        return max_p

