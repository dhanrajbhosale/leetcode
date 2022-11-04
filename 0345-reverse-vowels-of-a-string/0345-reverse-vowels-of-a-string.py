class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        l, r = 0, len(s_list)-1
        
        while l<r:
            while l<r and s_list[l] not in {'a','e','i','o','u','A','E','I','O','U'}:
                l+=1
            while l<r and s_list[r] not in {'a','e','i','o','u','A','E','I','O','U'}:
                r-=1
            if l<r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l+=1
                r-=1
        return "".join(s_list)
        