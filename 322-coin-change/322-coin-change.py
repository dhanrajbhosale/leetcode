class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Greedy apprach wont work here, we require reccursion, top down or bottom up with DP for optimization     
        
        # Solution 1 : Top Down Approach with DP
        memo = {} # dp
        cnt = 0
        def dfs(amount):
            if amount==0: # base case 
                return 0
            if amount <0: # it acts as an unbounded upper value for comparison.
                return float('inf')
            if amount in memo: # return if in dp
                return memo[amount]
            memo[amount] = 1+min([dfs(amount-c) for c in coins]) # take minimus from all paths
            return memo[amount]     
        
        minimum=dfs(amount)       
        return minimum if minimum < float('inf') else -1
