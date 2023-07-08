class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_r(x,y):
            return (x**2+y**2)**(1/2)
        pointes = sorted(points, key=lambda x: get_r(x[0],x[1]))
        return pointes[:k]
        