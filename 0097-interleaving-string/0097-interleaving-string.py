class Solution:
    # O(m*n) space
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1, s2, s3 = " "+s1, " "+s2, " "+s3 
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l+1:
            return False
        dp = [[False for _ in range(c)] for _ in range(r)]
        dp [0][0] = True
        for i in range(1, r):
            dp[i][0] = s3[i] == s1[i] and dp[i-1][0] 
        for j in range(1, c):
            dp[0][j] = s3[j] == s2[j] and dp[0][j-1] 
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i-1][j] and s1[i] == s3[i+j]) or (dp[i][j-1] and s2[j] == s3[i+j])
        return dp[-1][-1]