class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        checks=[0]*(l+1)
        for x in nums: 
            checks[x]=1
        return checks.index(0)
        