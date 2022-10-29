class Solution:
    # sol2 dp, recurssion top down TC O() SC O(n)
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def recc(n):
            if n<3: return n
            if dp[n]: return dp[n]
            dp[n]= recc(n-1)+recc(n-2)
            return dp[n]
        return recc(n)
        
    # sol1 dp iterative bottom up TC O(n) SC O(n)
    # def climbStairs(self, n: int) -> int:
    #     if n==1: return 1
    #     dp=[None]*(n+1)
    #     dp[1], dp[2]= 1, 2
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1]+dp[i-2]
    #     return dp[n]
    