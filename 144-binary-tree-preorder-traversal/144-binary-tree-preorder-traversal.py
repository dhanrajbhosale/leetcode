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
#         stack, res = [root], []
        
#         while stack:
#             node=stack.pop()
#             if node:
#                 # Print root, stack in order right, Left to pop later Left, Right
#                 res.append(node.val)
#                 stack.append(node.right)
#                 stack.append(node.left)            
#         return res
        
        # Morris Traversal Space O(1)
        res = []
        curr = root
        
        while curr:
            # If left null, print curr and move right
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            # before going left, make right most node on left subtree connected to current node, then go left
            else:
                prev = curr.left
                while prev.right and prev.right!=curr:
                    prev = prev.right
                # make thread and print ROOT
                if not prev.right:
                    prev.right = curr
                    res.append(curr.val)
                    curr = curr.left
                # if thread is already pointed to current node, means You have visited the node, cut the thread, and  move to the right
                else:
                    prev.right = None
                    curr = curr.right
        return res
            