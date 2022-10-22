import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        countT, window = defaultdict(int), defaultdict(int)
        for c in t: # store required dict
            countT[c]+=1
            
        l = 0 # left of current window   
        have, need = 0, len(countT) # unique char, have and need
        min_window = float('inf') 
        res = [-1, -1]
        
        for r in range(len(s)): # for every char in s
            char = s[r]
            window[char]+=1 # add char in window
            
            # if char is our need and if we get exact count required, increment have
            if char in countT and window[char]==countT[char]:
                have +=1
            
            # while we have all needed -  shrink window from left to get best, store min length
            while have == need:
                
                # store minimum window
                if (r-l+1) < min_window:
                    min_window = (r-l+1)
                    res = [l, r]
                
                window[s[l]]-=1
                # decrement have if removed char was needed and its cnt less that required
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                # shrink more
                l+=1
        l, r = res
        return s[l:r+1] if min_window!= float('inf') else ""