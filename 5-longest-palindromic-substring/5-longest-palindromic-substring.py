class Solution:
    # DP Solution, bottom Up
    # the row and col in the dp table represent the slicing index on the string s
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range (len(s))]
        # fill diagonal with 1 as all single char are pali
        
        for i in range(len(s)):
            dp[i][i] = True
        res=s[0]
        
        # fill only half table as i always should be < j
        for j in range(len(s)):
            for i in range(j):
                # in between it is pali or just 2 char so pali
                if s[i]==s[j] and (dp[i+1][j-1] or j-i==1):
                    dp[i][j]=True
                    if j-i+1>len(res):
                        res=s[i:j+1]
        return res
        
        
    # O(n^2) 
#     def longestPalindrome(self, s: str) -> str:
#         resLen=0
#         rL=0
#         rR=0
#         for i in range(len(s)):
#             # for odd
#             l,r=i,i
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if (r-l+1)>resLen:
#                     rL,rR=l,r+1
#                     resLen=r-l+1    
#                 l-=1
#                 r+=1
                
#             # for even
#             l,r=i,i+1
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if (r-l+1)>resLen:
#                     rL,rR=l,r+1
#                     resLen=r-l+1    
#                 l-=1
#                 r+=1
            
#         return s[rL:rR]
    