class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        masterMul = 1   
        zeroCnt = 0
        for i in nums:
            if i:
                masterMul*=i
            else:
                zeroCnt+=1
            if zeroCnt>=2:
                return [0]*len(nums)
            
        if zeroCnt==1:
            i = nums.index(0)
            nums = [0]*len(nums)
            nums[i] = masterMul
            return nums  
                
        for i in range(len(nums)):
            nums[i]=masterMul//nums[i]
        return nums
        
        
        