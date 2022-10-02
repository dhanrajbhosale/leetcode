class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort DFS
        vis, cycle = set(), set()
        res = []
        prer={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prer[crs].append(pre)
        
        # visited -> crs has been added to res
        # visiting -> crs not added to res but added to the cycle
        # unvisited -> crs not added to the res or cycle
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            
            cycle.add(crs)
            for i in prer[crs]:
                if not dfs(i):
                    return False
            cycle.remove(crs)
            vis.add(crs)
            res.append(crs)
            return True
            
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

                
        # this is topological sort problem
        # using BFS (Kahn's Algorithm)
        
#         inDegree = [0 for i in range(numCourses)]
#         adj = {i:[] for i in range(numCourses)}
#         res=[]
#         for crs, pre in prerequisites:
#             adj[crs].append(pre)
#             inDegree[pre]+=1
#         q = collections.deque()
        
#         for i in range(numCourses):
#             if inDegree[i]==0:
#                 q.append(i)
#         while q:
#             v = q.popleft()
#             res.append(v)
#             for i in adj[v]:
#                 inDegree[i]-=1
#                 if inDegree[i]==0:
#                     q.append(i)
#         return res[::-1] if len(res)==numCourses else []
    

    # 99.6% faster BFS 
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         # Create a prerequisite dict. (containing courses (nodes) that need to be taken (visited)
# 		# before we can visit the key.
#         preq = {i:set() for i in range(numCourses)}
# 		# Create a graph for adjacency and traversing.
#         graph = collections.defaultdict(set)
#         for i,j in prerequisites:
# 		    # Preqs store requirments as their given.
#             preq[i].add(j)
# 			# Graph stores nodes and neighbors.
#             graph[j].add(i)
        
#         q = collections.deque([])
# 		# We need to find a starting location, aka courses that have no prereqs.
#         for k, v in preq.items():
#             if len(v) == 0:
#                 q.append(k)
# 		# Keep track of which courses have been taken.
#         taken = []
#         while q:
#             course = q.popleft()
#             taken.append(course)
# 			# If we have visited the numCourses we're done.
#             if len(taken) == numCourses:
#                 return taken
# 			# For neighboring courses.
#             for cor in graph[course]:
# 			    # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
#                 preq[cor].remove(course)
# 				# If we've taken all of the preqs for the new course, we'll visit it.
#                 if not preq[cor]:
#                     q.append(cor)
# 		# If we didn't hit numCourses in our search we know we can't take all of the courses.
#         return []
                
        
        
        
