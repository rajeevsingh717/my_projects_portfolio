"""Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]] ## returning if there is only 1 row is requested
        ls = [[1]]
        i = 0
        while i < numRows-1: ## running the loop for n-1 rows, sinc the 1st row is added before
            last_set = ls[-1] ## picking up the last list in the main list. This list will be used to create the next list
            curr = [] ## initializing the new list to create the current list
            
            for j in range(0,len(last_set)+1):
                if j == 0: ## handling for the 1st element in the current list
                    curr.append(last_set[j])
                elif j == len(last_set): ## handling for the last element in the current list
                    curr.append(last_set[j-1])
                else: ## handling for all the elements in the first and last element in the current list
                    curr.append(last_set[j-1]+last_set[j])
            
            ls.append(curr)
            i += 1
        return ls
