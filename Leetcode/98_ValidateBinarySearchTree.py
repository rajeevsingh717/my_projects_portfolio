""" Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtreeof a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def iorderdfs(node, low=float(-inf), high=float(inf)):
            if not node:
                return True
            if node.val <= low or node.val >=high:
                return False
            
            print(node.right, node.val, high) 
            print(node.left,low, node.val)
            
            return dfs(node.right, node.val, high) and dfs(node.left,low, node.val ) 
        
        return dfs(root)
 

        
        
        



