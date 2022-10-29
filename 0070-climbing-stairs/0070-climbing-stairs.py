class Solution:
    # sol3 DP + Optimization (Bottom Up Approach)
    # To calculate the new value we only leverage the previous two values. So we don't need to use an array to store all the previous values.
    # Complexity : Time: O(n) ; Space: O(1)
    def climbStairs(self, n: int) -> int:
        if n<=1: return n
        prev1, prev2 = 1, 2
        for i in range(3, n+1):
            newVal = prev1 + prev2
            prev1 = prev2
            prev2 = newVal
        return prev2
        
    # sol2 dp iterative bottom up TC O(n) SC O(n)
    # def climbStairs(self, n: int) -> int:
    #     if n==1: return 1
    #     dp=[None]*(n+1)
    #     dp[1], dp[2]= 1, 2
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1]+dp[i-2]
    #     return dp[n]
    
    # sol1 dp, recurssion top down TC O(n) SC O(n)
    # def climbStairs(self, n: int) -> int:
    #     dp=[0]*(n+1)
    #     def recc(n):
    #         if n<3: return n
    #         if dp[n]: return dp[n]
    #         dp[n]= recc(n-1)+recc(n-2)
    #         return dp[n]
    #     return recc(n)
        
    
    