class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = []
        cnt = 0
        for x in sorted(intervals, key = lambda x: x[1]): #sort by end
            if res and x[0] < res[-1][1]: # remove overlapped one
                cnt += 1
            else:
                res.append(x)
        return cnt 