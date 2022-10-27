class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # store all 1s pos in list
        a_ones, b_ones = [], []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    a_ones.append((i,j))
                if B[i][j]==1:
                    b_ones.append((i,j))
                    
        # looping through the stored positions and computing the sliding patterns
        # If the sliding patterns match then it implies that, by sliding in the same way, we can converge one or more 1's
        d = collections.defaultdict(int)
        d[(0,0)]=0
        for t1 in a_ones:
            print("ss")
            for t2 in b_ones:
                t3 = (t2[0]-t1[0], t2[1]-t1[1])
                d[t3]+=1
        # return the max value of dic
        # return the value of the pattern shift with max 1 can overlap
        return max(d.values())
    