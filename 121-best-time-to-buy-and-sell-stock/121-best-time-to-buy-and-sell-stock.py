class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        mn=mx=prices[0]
        
        for i in range(len(prices)):
            mx=max(mx,prices[i]) #shift max to right new max
            if prices[i]<mn:
                mx=mn=prices[i] #shift min to next min, & max = min as max should be at right of min
            res=max(res,mx-mn) #update result
        return res
        