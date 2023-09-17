class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     s=""
    #     for i in digits:
    #         s+=str(i)
    #     num = str(int(s)+1)
    #     return [int(s) for s in num]
    
    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits