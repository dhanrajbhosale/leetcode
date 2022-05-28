class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Solution 1
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder

        
        # Solution 2
        # temp=nums
        # temp.sort()
        # for a in range(1,len(temp)):
        #     if temp[a-1]==temp[a]:
        #         return temp[a]
        
            
        