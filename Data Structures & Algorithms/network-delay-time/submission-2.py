class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        D=defaultdict(list)
        for u in times :
            D[u[0]].append((u[1],u[2]))
        min_heap = [(0, k)] 
        visited = set()
        max_time = 0
        
        while min_heap:
            time, u = heapq.heappop(min_heap) 
            if u in visited:
                continue
            
            visited.add(u)
            max_time = max(max_time, time)
            
            for v, w in D[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (time + w, v))
        return max_time if len(visited) == n else -1