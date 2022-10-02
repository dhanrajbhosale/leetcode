# TC O(N) SC(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # use nums[i] itself to store max till ith number
        # num[i] chose max from i-3 and i-2
        nums = [0,0,0] + nums
        for i in range(3, len(nums)):
            nums[i] = max(nums[i-3]+nums[i], nums[i-2]+nums[i])
        # return max from last two numbers
        return max(nums[-2], nums[-1])
        
    
        
        