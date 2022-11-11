class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2: return len(nums)
        cnt=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            cnt+=1
            nums[cnt]=nums[i]
        return cnt+1