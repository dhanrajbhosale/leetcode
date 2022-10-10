class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l= len(palindrome)
        if l<=1:
            return ""
        for i in range(l):
            if palindrome[i]!="a" and (i!=l//2 or l%2==0):
                palindrome=palindrome[:i]+"a"+palindrome[i+1:]
                break
            if i==l-1:
                palindrome=palindrome[:i]+"b"+palindrome[i+1:]
        return palindrome
                
                
        