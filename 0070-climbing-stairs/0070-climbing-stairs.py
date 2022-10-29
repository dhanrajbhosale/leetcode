class Solution:
    # sol1 dp bottom up TC O(n) SC O(n)
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        dp=[None]*(n+1)
        dp[1], dp[2]= 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]