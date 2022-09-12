# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # root right left traversal
        res=[]
        def recursion(root, level, res):
            if not root:
                return
            if level==len(res):
                res.append(root.val)
            recursion(root.right, level+1, res)
            recursion(root.left, level+1, res)
        recursion(root, 0, res)
        return res
        
    
        