# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:		
    # dictionary with the keys being its vertical placement and the value being a tuple of (level, root.val). I then sort the dictionary based on keys and sort it again based on level.
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.helper(0,0, root, dic)
        
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)    
        return result
    
    def helper(self, placement, level, root, dic):
        if not root:
            return
        dic[placement].append((level, root.val))
        self.helper(placement-1, level+1, root.left, dic)
        self.helper(placement+1, level+1, root.right, dic)
            