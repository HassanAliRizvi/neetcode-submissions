# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from collections import deque

        """
        q = [5] p = 3 q = 8
        q.append(left_child,right_child)
        parent = q.popleft()
        
        [3,8]
        iterate through the queue and check if p and q are there
        if so return parent otherwise keep lopping using the while loop
        if p == q.popleft():
        
        """

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


        """
        Failed BFS APPROACH because what if p or q is NOT the children of the popped element?

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right # [5,3,8]
            if left and right:
                if ((left.val == p.val and right.val == q.val) or
                    (left.val == q.val and right.val == p.val)):
                    return node
            
            if node.val == p.val:
                if ((left and left.val == q.val) or 
                    (right and right.val == q.val)):
                    
                    return node
            
            if left:
                queue.append(left)

            if right:
                queue.append(right)

        """
    

        