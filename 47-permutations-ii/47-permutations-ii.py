class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(num, subset):
            if len(num)<=0:
                res.append(subset[:])
                return
            for i in range (len(num)):
                if i>0 and num[i]==num[i-1]:
                    continue
                dfs(num[:i]+num[i+1:], subset+[num[i]])   
        dfs(nums, [])
        return res