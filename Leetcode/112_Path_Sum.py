"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # ls = []
        if root is None:
            return False
        queue = [(root, root.val)]
        while queue:
            node, sum_sofar = queue.pop(0)
            # ls.append(node.val)
            # print(ls)
            
            if sum_sofar == targetSum and node.left is None and node.right is None:
                return True
            if node.left : queue.append((node.left, node.left.val + sum_sofar))
            if node.right : queue.append((node.right, node.right.val + sum_sofar))
        
        return False
        
        
