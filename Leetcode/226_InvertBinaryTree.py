Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## implemented using recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): ## create DFS function to iterate through each node
            if not node:
                return None
            else:
                node.left, node.right = node.right , node.left ## swap the node
            ## call the dfs function again for left and right node
            dfs(node.left) 
            dfs(node.right)
             
        dfs(root)
        return root

