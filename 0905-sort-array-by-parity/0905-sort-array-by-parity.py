class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A)-1

        while i<j:
            if A[i]%2>A[j]%2: # if wrong, swap
                A[i], A[j] = A[j], A[i]
            if A[i]%2 ==0: i+=1 # if even, just skip by i++
            if A[j]%2 ==1: j-=1 # if odd, just skip by j--
        return A