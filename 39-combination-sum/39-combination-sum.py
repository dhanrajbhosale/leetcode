# Approach 1
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res=[]     
#         def dfs(i, subset, total):
#             if target==total:
#                 res.append(subset[:])
#                 return 
#             if i>=len(candidates) or target<total:
#                 return        
#             #decision to take and START FROM SAME POINT with less sum
#             subset.append(candidates[i])
#             dfs(i, subset, total+candidates[i])
#             #decision not to take
#             subset.pop()
#             dfs(i+1, subset, total)
            
#         dfs(0, [], 0)
#         return res

# approach 2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]    
        candidates.sort()
        def dfs(cands, subset, target):
            if target<0:
                return
            if target == 0:
                res.append(subset[:])
                return
            for i in range (len(cands)):
                if cands[i] > target:  #here  
                    break
                # if cands[i]>target:
                #     break
                dfs(cands[i:], subset+[cands[i]], target-cands[i])    
            
        dfs(candidates, [], target)
        return res    