class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)

        pq = [(grid[0][0], 0, 0)]
        
        visited = set()
        visited.add((0, 0))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    new_time = max(t, grid[nr][nc])
                    
                    heapq.heappush(pq, (new_time, nr, nc))
                    
        return -1