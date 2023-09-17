class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)
        

        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf