""" Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        lst = []

        for m in range(row):
            for n in range(col):
                if matrix[m][n] == 0:
                    print(matrix[m][n])

                    ## Saving the row locations to list
                    for i in range(row):
                        lst.append([i,n])
                        
                    ## Saving the col locations to list
                    for i in range(col):
                        lst.append([m,i])
        
        ## setting all the targetted locaion to 0
        for row, col in lst:
            matrix[row][col] = 0                      
              


            
