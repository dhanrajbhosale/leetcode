class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        
        prev=self.generate(numRows-1)
        temp=prev[numRows-2]
        res=[[1]]
        for i,v in enumerate(temp):         
            if i==(numRows-2):
                break
            res[0].append(v+temp[i+1])
        res[0].append(1)
        return prev+res
            