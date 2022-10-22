import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c]+=1    
        l = 0   
        have, need = 0, len(countT) 
        min_window = float('inf') 
        res = [-1, -1]
        
        for r in range(len(s)):
            char = s[r]
            window[char]+=1
            
            if char in countT and window[char]==countT[char]:
                have +=1
            while have == need:
                if (r-l+1) < min_window:
                    min_window = (r-l+1)
                    res = [l, r]
                
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l:r+1] if min_window!= float('inf') else ""