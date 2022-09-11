# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recurssive
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []
        
        # iterative
        stack, res = [root], []
        
        while stack:
            node=stack.pop()
            if node:
                # Print root, stack in order right, Left to pop later Left, Right
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)            
        return res
            
    
    