from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)
        # graph = {i : [] for i in range(n)}
        def get_manhattan_dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        # Connect each pair of points with a weighted edge
        for i in range(n):
            for j in range(i+1, n):
                dist = get_manhattan_dist(points[i], points[j])
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        # implement minimum spanning tree
        # prim's algorrithm
        # point, cost
        res = 0
        visited = set()
        minHeap = [[0, 0]]
        
        while len(visited)<n:
            cost, i = heapq.heappop(minHeap)
            if i in visited: 
                continue
            res+= cost
            visited.add(i)
            
            
            for neiCost, nei in graph[i]:
                if nei not in visited:
                    # he heap will be sorted based on the first element of each item in the heap 
                    heapq.heappush(minHeap, [neiCost, nei])
            
        return res
                
        
        