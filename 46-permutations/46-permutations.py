from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(num, subset):
            if len(num)<=0:
                res.append(subset[:])
                return
            for i in range(len(num)):
                dfs(num[:i]+num[i+1:], subset+[num[i]])    
        dfs(nums, [])
        return res
        
            