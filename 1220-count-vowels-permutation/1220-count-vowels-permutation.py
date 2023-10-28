class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n==1:
            return 5
        mod = 10**9 + 7
        char_suffix = {
                       '#': ['a','e','i','o','u'], # place holder for start point
                       'a':['e'],
                       'e':['a', 'i'],
                       'i':['a','e','o','u'],
                       'o':['i','u'],
                       'u':['a']
                       }
        dp = {}
        # pass current char index and char
        # return (n-char_index) lenghth word combinations starting with char
        def recursion(char_index, char):
            if char_index==n:
                return 1
            if (char_index, char) in dp:
                return dp[(char_index, char)]
            total=0
            for next_c in char_suffix[char]:
                total+=recursion(char_index+1, next_c)
            dp[(char_index, char)]=total
            return total%mod

        return recursion(0, '#')%mod