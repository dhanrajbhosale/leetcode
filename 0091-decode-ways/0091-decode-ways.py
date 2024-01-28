class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=N:
                return 1
            # if the first character is 0 then cant decode
            if s[i]=='0':
                return 0
            if i==N-1:
                return 1
            # two options
            # decode 1 digit or decode 2 digits
            ans = dfs(i+1)
            if int(s[i:i+2])<=26:
                ans += dfs(i+2)
            memo[i]=ans
            return ans

        return dfs(0)