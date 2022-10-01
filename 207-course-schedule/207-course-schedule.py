class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycle using BFS
        adj = {i: [] for i in range(numCourses)} 
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
		# traverse the graph starting at each vertex
        for v in range(numCourses):
            bfs = deque(adj[v]) # add all the neighbours of starting node to the BFS queue
            visited = set() # use a set to keep track of the visited nodes and not get stuck in a cycle
            
            while bfs:
                current = bfs.pop()
                visited.add(current)
                if current == v: # we ended up at the same vertex where we started - there's a cycle
                    return False
                for n in adj[current]: # cycle not detected, continue the traversal to the next nodes
                    if n not in visited:
                        bfs.appendleft(n)                 
        return True
       
        
        # detect cycle using DFS
        # like normal dfs, we dont need to avoid parent as adj list are not given.. we are creating that list using prer list so already parent node is not present.
        
        # vis = set()
        # adj  = {i:[] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     adj[crs].append(pre)
        # def dfs(node):
        #     if adj[node]==[]:
        #         return True
        #     if node in vis:
        #         return False
        #     vis.add(node)
        #     for i in adj[node]:
        #         if not dfs(i): return False
        #     vis.remove(node)
        #     adj[node]=[]
        #     return True
        # # to consider disconnected graphs
        # for i in range(numCourses):
        #     if(not dfs(i)): 
        #         return False
        # return True