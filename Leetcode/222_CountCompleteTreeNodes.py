"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
                return 0

        queue = [root] ## adding the root into the list
        count = 0

        while queue: ## check until queue is empty
            root = queue.pop(0) ## pop the 1st element from the queue from the front
            count += 1 ## increase the counter

            if root.left: 
                queue.append(root.left) ## add the left node to end of queue if it exists
            
            if root.right:
                queue.append(root.right) ## add the right node to end of queue if it exists
            
        
        return count

