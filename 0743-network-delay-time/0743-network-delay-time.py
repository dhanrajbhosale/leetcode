# Standard Djikstraa
# O (E * log V)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append([w, v])
            # adj[v].append([w, u])
        
        # edge, destination
        minHeap = [[0, k]] 
        visited = set()
        ans = 0
        # while len(visited)<n:
        while minHeap:
            path, source = heapq.heappop(minHeap)
            if source in visited:
                continue
            visited.add(source)
            ans = max(ans, path)
            for edge, destination in adj[source]:
                if destination in visited:
                    continue 
                heapq.heappush(minHeap, [path+edge, destination])
            
        # if not visited all nodes, return -1
        return ans if len(visited)==n else -1
            