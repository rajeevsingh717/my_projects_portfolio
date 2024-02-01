"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(i, j):
          if i < 0 or i >= len(grid) or j< 0 or j >=len(grid[0]) or grid[i][j]=="0":
            return
         
          grid[i][j] = "0"
          
          dfs(i+1,j)
          dfs(i-1,j)
          dfs(i,j+1)
          dfs(i,j-1)
        
        for row in range(len(grid)):
          for col in range(len(grid[0])):
            if grid[row][col] == "1":
              count += 1
              dfs(row, col)
        
        return count
        
        
