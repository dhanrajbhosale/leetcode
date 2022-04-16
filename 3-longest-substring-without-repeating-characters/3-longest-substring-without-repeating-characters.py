class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet=set()
        #window left pointer
        l=0
        res=0
        #window right pointer
        for r in range(len(s)):
            # if duplicate, start removing from left side until no duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
                
        