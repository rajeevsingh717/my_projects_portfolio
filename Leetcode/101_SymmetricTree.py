"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Input: root = [1,2,2,3,4,4,3]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(left, right):
            if left is None and right is None:
                return True  ## returing True because even if one False is found in any pair comparison then final result will become False. To validate as symmetrical tree every pair has to match.
            
            if left is None or right is None: ## return False when the tree is not balanced
                return False
            return left.val == right.val and ismirror(left.left, right.right) and ismirror(left.right, right.left) ## expression to combine current comparison and the future comparison
            
        if root is None:
            return False
        
        flg = ismirror(root.left,root.right)
        return flg
        
## Trick - This is recursive way. Calling back the recursive function by pair which needs to be compared 
