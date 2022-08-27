class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort() # for avoiding dupicates 
        def dfs(cands, subset, target):
            if target<0:
                return
            if target==0:
                res.append(subset[:])
                return
            for i in range (len(cands)):
                if i > 0 and cands[i] == cands[i-1]:
                    continue
                # if target<cands[i]:
                #     break
                dfs(cands[i+1:], subset+[cands[i]], target-cands[i])
            
        dfs(candidates, [], target)    
        return res