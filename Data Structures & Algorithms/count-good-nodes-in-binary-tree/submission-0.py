# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs_function(root,max_value):
            max_val = max_value
            if not root:
                return 0
            
            node_count = 0
            
            if root.val >= max_val:
                max_val = root.val
                node_count += 1

            left = dfs_function(root.left,max_val)
            right = dfs_function(root.right,max_val)

            return node_count + left + right
        
        return dfs_function(root,root.val)