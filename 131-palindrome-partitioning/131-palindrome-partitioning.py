class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @functools.lru_cache(len(s))
        def dfs(start):
            if start == len(s):
                return [[]]
            res = []
            for i in range(start, len(s)):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    res += [[cur] + rest for rest in dfs(i+1)]
            return res
        return dfs(0)