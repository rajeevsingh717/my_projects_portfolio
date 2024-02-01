"""Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        
        self.mindiff = float(inf)
        self.prev_node = None
        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                
                if self.prev_node is not None:
                    self.mindiff = min(self.mindiff,node.val - self.prev_node.val )
                self.prev_node = node
                
                dfs(node.right)

        dfs(root)
        return self.mindiff

