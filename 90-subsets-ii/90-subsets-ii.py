class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() # imp to skip duplicates 
        def backtracking(i, subset):
            # base case- end of the input array
            if i>=len(nums):
                res.append(subset[:])
                return
            # decision to take
            subset.append(nums[i])
            backtracking(i+1, subset)
            # decision to not take
            while i+1<len(nums) and nums[i]==nums[i+1]: # skips duplicate
                i+=1
            subset.pop()
            backtracking(i+1, subset)
        backtracking(0, [])
        return res
            
