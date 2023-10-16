class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N = len(s)
        res=[]
        min_len = float('inf')
        for diff in range(k, N+1):
            for i in range(N-diff+1):
                temp = s[i:i+diff]
                if temp.count('1')>=k:
                    if diff>min_len and len(res)>=1:
                        break
                    res.append(temp)
                    min_len = min(min_len, len(temp))
            if diff>min_len and len(res)>=1:
                        break
        res.sort()
        return res[0] if res else ""