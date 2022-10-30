class Solution:
    # sol 2 - need not to compare all strings
    # just sort list and compare first and last string
    # as all midlle will be lexographically sorted
    def longestCommonPrefix(self, m: List[str]) -> str:
        if not m: return ''
        m.sort()
        s1, s2 = m[0], m[-1]

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
    
    # sol 1
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs)==1: return strs[0]
    #     def commonPref(s1, s2):
    #         s1_list, s2_list = list(s1), list(s2)
    #         res = ""
    #         for i in range(min(len(s1_list), len(s2_list))):
    #             if s1_list[i]==s2_list[i]:
    #                 res+=s1_list[i]
    #             else:
    #                 break
    #         return res
    #     LCP = strs[0]
    #     for s in strs:
    #         LCP = commonPref(LCP, s)            
    #     return LCP