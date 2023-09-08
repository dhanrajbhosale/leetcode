from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks).values()
        max_heap = [-c for c in cntr] # as py dont have max heap so using min heap as max heap
        heapq.heapify(max_heap)
        time = 0
        # queue to store remianing task freq and time when it will be available
        q = deque()
        
        while max_heap or q:
            time += 1
            
            if max_heap:
                # get hi freq task
                task = heapq.heappop(max_heap) + 1
                if task:
                    q.append((task, time + n))
            
            # task available, push it to heap again
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
