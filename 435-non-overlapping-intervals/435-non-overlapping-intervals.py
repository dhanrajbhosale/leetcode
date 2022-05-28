class Solution(object):
    def eraseOverlapIntervals(self, A):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        out=[]
        print(sorted(A,key=lambda i:(i[0],i[1])))
        for a in sorted(A,key=lambda i:(i[0],i[1])):
            if out and out[-1][1]>a[0]: #two are overlapping, need to skip any one
                if out[-1][1]>a[1]:     #skip big range - if latest added is > current
                    out[-1]=a
            else:
                out+=[a]
        return len(A)-len(out)
                