class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        num = str(int(s)+1)
        return [int(s) for s in num]