# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # do horizontal traversal and just add level reverse alternatively
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res=[]
        isLeftToRight = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
            if level:
                # adding level reverse alternatively
                if isLeftToRight:
                    res.append(level[::-1])
                    isLeftToRight = False
                else:
                    res.append(level)
                    isLeftToRight = True
        return res
                