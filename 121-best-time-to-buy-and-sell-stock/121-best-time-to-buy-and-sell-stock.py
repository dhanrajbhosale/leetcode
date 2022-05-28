class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        mn=mx=prices[0]
        
        for i in range(len(prices)):
            mn=min(mn,prices[i])
            res=max(res,prices[i]-mn) 
        return res
        