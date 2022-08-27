class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def dfs(i, subset, total):
            if target==total:
                res.append(subset[:])
                return 
            if i>=len(candidates) or target<total:
                return
            
            #decision to take and START FROM SAME POINT with less sum
            subset.append(candidates[i])
            dfs(i, subset, total+candidates[i])
            #decision not to take
            subset.pop()
            dfs(i+1, subset, total)
            
        dfs(0, [], 0)
        return res