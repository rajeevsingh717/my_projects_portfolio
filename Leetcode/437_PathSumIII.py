""" Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs (node, running_sum):
            nonlocal result
            if not node:
                return
            
            running_sum += node.val

            if running_sum - targetSum in sum_count:
                result += sum_count[running_sum - targetSum] ## if found in the dictionary then add the value to result variable

            
            sum_count[running_sum] += 1 ## Since its a default dictionary it will append if its entirely new sum or increment the value by 1 if it already eixts there

            dfs(node.left, running_sum) ## keep going left of tree
            dfs(node.right, running_sum) ## keep going right of tree

            sum_count[running_sum] -= 1 ## this is to reduce the count of running_sum by 1 once path backtracks to the parent node

        result = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1 ## for the root node if any sum which is equal to target and has root node
        dfs(root,0)

        return result
        


        
