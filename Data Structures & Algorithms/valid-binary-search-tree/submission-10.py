# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_dfs(node,lower_bound,upper_bound):
            if not node:
                return True
            
            if lower_bound is not None and lower_bound >= node.val:
                return False
            
            if upper_bound is not None and upper_bound <= node.val:
                return False
            
            left = valid_dfs(node.left,lower_bound,node.val)
            right = valid_dfs(node.right,node.val,upper_bound)
            

            return left and right

        return valid_dfs(root,None,None)
            
