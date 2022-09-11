class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Greedy apprach wont work here, we require reccursion, 
        # top down or bottom up with DP for optimization     
        
        # Solution 1 : Top Down Approach with DP
        # memo = {} # dp
        # cnt = 0
        # def dfs(amount):
        #     if amount==0: # base case 
        #         return 0
        #     if amount <0: # it acts as an unbounded upper value for comparison.
        #         return float('inf')
        #     if amount in memo: # return if in dp
        #         return memo[amount]
        #     memo[amount] = 1+min([dfs(amount-c) for c in coins]) # take minimus from all paths
        #     return memo[amount]          
        # minimum=dfs(amount)       
        # return minimum if minimum < float('inf') else -1
    
        # Solution 2: Bottom Up approach with DP
        dp=[amount+1]*(amount+1) # dp with max value that wont be iin calculation (infinite, but here amount+1 will work)
        dp[0]=0 # base case: for amount 0, 0 coins required        
        for a in range(1, amount+1): # compute coins required for all amount
            for c in coins: # compute with each coin
                if c<=a: # only if coin value will small than amount
                    dp[a]=min(dp[a], 1+dp[a-c]) # ex. if coin 3 is using, dp[7]=1+dp[4]                  
        return dp[amount] if dp[amount]!=amount+1 else -1                    
            