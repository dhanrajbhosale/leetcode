# substring by power set approach (bit manipulation)
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # [1/0,1/0,1/0] represents given nums [1,2,3] - to take or not to take 
#         res=[]
#         l=len(nums)
#         for i in range(1<<l): # 2 POWER l combinations
#             tmp=[]
#             for j in range(l): # bit for all elements in given nums list
#                 if i & (1<<j): # checking if i th bit is set
#                     tmp.append(nums[j]) # making 1 combination
#             res.append(tmp) # adding one combination in list
#         return res
    
# backtracking - dfs Time O(n*2^n) (Cant make more efficient as all subset 2^n to be calculated)
class Solution:
    def subsets(self, nums:List[int])-> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # decision to include
            subset.append(nums[i])
            dfs(i+1)
            # decision to exclude
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res