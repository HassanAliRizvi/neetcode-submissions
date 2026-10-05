# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  

        """

        Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        preorder[0] = root
        inorder[1] = root
        we look at left and right of that root
        1.left = 2
        1.right = 3.right = 4

        """
        inorder_dict = {v:i for i,v in enumerate(inorder)}
        preorder_idk = 0
        def helper(l,r):
            nonlocal preorder_idk
            if l > r:
                return None
            
            root_value = preorder[preorder_idk]
            middle = inorder_dict[root_value]
            root = TreeNode(root_value)

            preorder_idk += 1

            root.left = helper(l,middle-1)
            root.right = helper(middle+1,r)

            return root
        
        return helper(0,len(inorder)-1)




        

        