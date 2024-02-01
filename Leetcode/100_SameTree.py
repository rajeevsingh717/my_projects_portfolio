"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and node2:
                return False
            elif node1 and not node2:
                return False
            elif not node1 and not node2:
                return  True
            elif node1.val != node2.val:
                return False   
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            
        return dfs(p,q)
