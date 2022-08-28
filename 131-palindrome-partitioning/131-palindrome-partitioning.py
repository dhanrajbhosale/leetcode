class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.dfs(s, [], res)
        return res
    
    def isPal(self, s):
        return s==s[::-1]
        
    def dfs(self, s, subset, res):
        if not s:
            res.append(subset[:])
            return
        # if just len(s), 'i' max will be len(s)-1, which will ignore the case of including last character during slicing.
        for i in range(1,len(s)+1):         
            if self.isPal(s[:i]):
                self.dfs(s[i:], subset+[s[:i]], res)
                
        
        