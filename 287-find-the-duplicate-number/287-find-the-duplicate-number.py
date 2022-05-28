class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=nums
        temp.sort()
        for a in range(1,len(temp)):
            if temp[a-1]==temp[a]:
                return temp[a]
        
            
        