# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recurrsive approach Time O(n) Space O(n) auxilary stack space
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []
        
        # iterative approach Time O(n) Space O(n)
        # stack, res = [], []      
        # while True:
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     if not stack: return res
        #     node = stack.pop()
        #     res.append(node.val)
        #     root=node.right
            
        # Approach 3 rd - Morris Traversal Without Stack (using threaded BT) And Recurrsion Time O(n) Space O(1)
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
                # make thread
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                # if thread is already pointed to current node, means You have visited the node, cut the thread, print the root and  move to the right
                else:
                    prev.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
                    
                    
                    
                