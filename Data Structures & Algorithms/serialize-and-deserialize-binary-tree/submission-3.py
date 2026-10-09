# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        
        root_string = str(root.val)
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return root_string + ',' + left + ',' + right
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 1,2,3,null,null,4,5 
        # [1]
        res = data.split(",")
        self.i = 0

        def build():
            if res[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(res[self.i])
            self.i += 1

            node.left = build()
            node.right = build()

            return node
        
        return build()

        

            



