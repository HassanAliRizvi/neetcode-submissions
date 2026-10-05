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
        inorder_dict = {i:v for v,i in enumerate(inorder)}
        preorder_index = 0

        def build(left,right):
            nonlocal preorder_index

            if left > right:
                return None
            
            value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(value)
            middle = inorder_dict[value]

            root.left = build(left,middle-1)
            root.right = build(middle+1,right)

            return root
        
        return build(0, len(inorder)-1)




        

        