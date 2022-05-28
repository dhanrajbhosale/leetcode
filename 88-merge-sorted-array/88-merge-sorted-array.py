class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Solution 1
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]: #nums1 start from last if num 1>2 add it to last
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1                              #take next num1
            else:
                nums1[m + n - 1] = nums2[n - 1]   #add num2 to the last
                n -= 1
        
        #Solution 2
        # nums1[m:]=nums2
        # nums1.sort()