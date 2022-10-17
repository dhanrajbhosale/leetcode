class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ss=""
        for i in s:
            if (ord('a')<=ord(i) and ord(i)<=ord('z')) or (ord('0')<=ord(i) and ord(i)<=ord('9')):
                ss+=i
        return ss[:]==ss[::-1]