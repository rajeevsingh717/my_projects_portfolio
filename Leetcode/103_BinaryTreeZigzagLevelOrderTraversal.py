"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        
        if not root:
            return array

        def dfs(node, level):
            print(array, len(array), level)
            if len(array) == level:
                array.append([])
            
            if level % 2 == 0:
                array[level].append(node.val)
            else:
                array[level].insert(0, node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return array
