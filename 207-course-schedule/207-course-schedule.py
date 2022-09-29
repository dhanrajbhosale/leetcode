class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycle using DFS
        # like normal dfs, we dont need to avoid parent as adj list are not given.. we are creating that list using prer list so already parent node is not present.
        
        vis = set()
        adj  = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        def dfs(node):
            if adj[node]==[]:
                return True
            if node in vis:
                return False
            vis.add(node)
            for i in adj[node]:
                if not dfs(i): return False
            vis.remove(node)
            adj[node]=[]
            return True
        # to consider disconnected graphs
        for i in range(numCourses):
            if(not dfs(i)): 
                return False
        return True