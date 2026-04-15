class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        
        # Priority Queue stores: (current_water_level, row, col)
        # We start at (0,0), so the initial time is the elevation at (0,0)
        pq = [(grid[0][0], 0, 0)]
        
        # Keep track of visited cells to avoid cycles
        visited = set()
        visited.add((0, 0))
        
        # Directions: Up, Down, Left, Right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            # 1. Greedy Step: Always pick the path with the lowest water level so far
            t, r, c = heapq.heappop(pq)
            
            # 2. Target Reached?
            if r == N - 1 and c == N - 1:
                return t
            
            # 3. Explore Neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if visited
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # 4. The Logic Shift:
                    # The time to enter the new cell is the max of:
                    # - The current water level (t)
                    # - The elevation of the new cell (grid[nr][nc])
                    new_time = max(t, grid[nr][nc])
                    
                    heapq.heappush(pq, (new_time, nr, nc))
                    
        return -1