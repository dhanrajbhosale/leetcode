class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # cl is window lenghth     
        for cl in range(2, n+1):
            for i in range(0, n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and cl==2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j-1])
        return dp[0][n-1]
        