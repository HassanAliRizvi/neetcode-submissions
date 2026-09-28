# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        [1,2,3] are there childs right hand side of 3? If yes append to a result list
        is there a left child of 3? If so append 
        If not left and right child of 3 then check is there a right child of 2? if yes then
        append that child to result list
        If no then append left child of 2

        """
        from collections import deque
        q = deque()
        q.append(root)
        if not root:
            return []
        res = [root.val]
        #level = 0
        while q:
            level = None
            for _ in range(len(q)):
                node = q.popleft()
                left = node.left
                right = node.right
                if right:
                    q.append(right)
                if left:
                    q.append(left)
                if level==None and right:
                    level = right.val
                    res.append(level)
                if level==None and (not right and left):
                    level = left.val
                    res.append(level)
        
        return res

        """
        [4]

        """


        