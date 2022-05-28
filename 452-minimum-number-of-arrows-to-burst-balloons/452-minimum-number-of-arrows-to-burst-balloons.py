class Solution(object):
    def findMinArrowShots(self, A):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=[]
        for a in sorted(A, key=lambda i:i[0]):
            if res and res[-1][1]>=a[0]:
                res[-1][1]=min(res[-1][1],a[1])
            else:
                res+=[a]
        return len(res)
        