class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # this is topological sort problem
        # using BFS (Kahn's Algorithm)
        
        inDegree = [0 for i in range(numCourses)]
        adj = {i:set() for i in range(numCourses)}
        res=[]
        for crs, pre in prerequisites:
            adj[crs].add(pre)
            inDegree[pre]+=1
        q = collections.deque()
        
        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)
        while q:
            v = q.popleft()
            res.append(v)
            for i in adj[v]:
                inDegree[i]-=1
                if inDegree[i]==0:
                    q.append(i)
        return res[::-1] if len(res)==numCourses else []
                
        
        
        
