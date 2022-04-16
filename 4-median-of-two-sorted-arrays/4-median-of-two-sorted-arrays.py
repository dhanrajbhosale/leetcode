class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=nums1+nums2
        num.sort()
        i=0
        l=len(num)
        res=0
        while i<l/2:
            i+=1         
        res= (num[i-1]+num[i])/2.0 if l%2==0 else num[i]
        return res