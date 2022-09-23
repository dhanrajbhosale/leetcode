# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return 0
            # calculate height of the left and right side
            left = dfs(root.left)
            right = dfs(root.right)
            # store max PATH for that path
            res[0]= max(res[0], left + right)
            
            # return the max HEIGHT of that node
            return 1 + max(left, right)
        dfs(root)
        
        return res[0]
        
        
        
        
        