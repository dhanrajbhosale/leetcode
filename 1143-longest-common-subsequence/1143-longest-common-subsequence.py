class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        r = len(s1)
        c = len(s2)  
        # consider 1 base indexing, if i=0 or j = 0 make it 0, as no common 
        dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1, r+1):
            for j in range(1, c+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[r][c]
                
