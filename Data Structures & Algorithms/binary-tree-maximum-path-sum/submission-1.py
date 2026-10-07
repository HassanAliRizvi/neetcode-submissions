# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = root.val
        def dfs(node):
            nonlocal path_sum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur_path = max(left+node.val,right+node.val,node.val)
            path_sum = max(path_sum,cur_path,node.val+left+right)

            return cur_path
        
        dfs(root)
        return path_sum


        