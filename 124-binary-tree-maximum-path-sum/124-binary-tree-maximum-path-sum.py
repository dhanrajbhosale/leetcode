# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     Approch: calculate sum of left and right, update result if left right and curent node total is max, this max is for path from that current node, now return the max from left or right to parent node (only if greater than zero) to form other path combinations
 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # storing max sum including current node
            res = max(res, root.val + left + right)
            # returning left or rigt to form next path onlt if it's greater than ZERO, as -ve number won't add value
            return max(0, left + root.val, right + root.val)
        dfs(root)      
        return res
    