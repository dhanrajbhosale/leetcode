# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recurssive
        # return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []
        
        # Iterrative 1 JUST REVERSE THE PREORDER - Left Right Root <-> Root Right Left
        stack, res = [root], []
        
        while stack:
            node= stack.pop()
            if node: # 
                res.append(node.val)
                stack.append(node.left) 
                stack.append(node.right)
        return res[::-1]
                
        
        