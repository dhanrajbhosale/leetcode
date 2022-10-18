class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s = self.countAndSay(n-1)
        i, l, temp =0, len(s), s[0]
        res, cnt = "", 0
        while i<l:
            while i<l and temp==s[i]:
                cnt+=1
                i+=1
            res+=str(cnt)+ temp
            if i<l:
                temp = s[i]
            cnt=0
        return res
        