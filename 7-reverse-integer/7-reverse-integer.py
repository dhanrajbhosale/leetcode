class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0: 
            return 0
        res=""
        negflag=1
        
        if x<0:
            x=-x
            negflag=-1
        q=x
        while q!=0:
            q,r =divmod(x,10)
            res+=str(r)
            x=q         
        return int(res)*negflag if -(2**31)-1 < int(res)*negflag < 2**31 else 0
        