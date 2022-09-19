class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=0
        rL=0
        rR=0
        for i in range(len(s)):
            # for odd
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    rL,rR=l,r+1
                    resLen=r-l+1    
                l-=1
                r+=1
                
            # for even
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    rL,rR=l,r+1
                    resLen=r-l+1    
                l-=1
                r+=1
            
        return s[rL:rR]
    