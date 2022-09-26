"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # hashmap to store old to new pair
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # append current nodes neighbors to copy's neighbour 
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy    
        
        return dfs(node) if node else None