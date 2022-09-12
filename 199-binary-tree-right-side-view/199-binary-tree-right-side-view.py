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
        self.recursion(root, 0, res)
        return res
        
    def recursion(self, root, level, res):
        if not root:
            return
        if level==len(res):
            res.append(root.val)
        self.recursion(root.right, level+1, res)
        self.recursion(root.left, level+1, res)
        