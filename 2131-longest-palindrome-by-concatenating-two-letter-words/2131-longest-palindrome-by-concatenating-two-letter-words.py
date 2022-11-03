class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = collections.defaultdict(lambda: [0,0])
        cnt = 0
        isMid = False
        
        for w in words:
            if w[0]==w[1]:
                dic[w][0]+=1
                dic[w][1]= -1
            elif w[0]<w[1]:
                dic[w][0]+=1
            else:
                dic[w[1]+w[0]][1]+=1
        for i in dic.values():
            # if 'cc', 
            if i[1]==-1:
                if i[0]%2==1: isMid=True
                cnt+= 4*(i[0]//2)
            else:
                cnt+=4*min(i)      
        if isMid:
            cnt+=2
        return cnt
                
        