# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        if not root:
            return []

        q = deque()
        q.append(root)
        res = [[root.val]]
        while q:
            res1 = []
            for _ in range(len(q)):
                node = q.popleft()
                left = node.left
                right = node.right

                #res1.append(node.val)

                if left:
                    q.append(left)
                    res1.append(left.val)
                if right:
                    q.append(right)
                    res1.append(right.val)

            if res1 != []:
                res.append(res1)

        
        return res
        