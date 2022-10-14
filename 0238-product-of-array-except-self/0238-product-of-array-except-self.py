class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left to right, right to left
        res = [1] * len(nums)
        
        preFix = 1
        for i in range(len(nums)):
            res[i] = preFix
            preFix *=nums[i]
        
        postFix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postFix
            postFix *=nums[i]

        return res
            
            
#       broot force
#         masterMul = 1   
#         zeroCnt = 0
#         for i in nums:
#             if i:
#                 masterMul*=i
#             else:
#                 zeroCnt+=1
#             if zeroCnt>=2:
#                 return [0]*len(nums)
            
#         if zeroCnt==1:
#             i = nums.index(0)
#             nums = [0]*len(nums)
#             nums[i] = masterMul
#             return nums  
                
#         for i in range(len(nums)):
#             nums[i]=masterMul//nums[i]
#         return nums