class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_sold = []
        for i in range(len(mat)):
            num_sold.append([sum(mat[i]), i])
        num_sold.sort(key= lambda x:x[0])
        return [num_sold[i][1] for i in range(k)]
        