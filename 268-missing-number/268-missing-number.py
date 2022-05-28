class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Solution 1
        n = len(nums)
        return n * (n+1) / 2 - sum(nums) #sum of n terms - sum of list
        
        #Solution 2
#         l=len(nums)
#         checks=[0]*(l+1)
#         for x in nums: 
#             checks[x]=1
#         return checks.index(0)
        
        