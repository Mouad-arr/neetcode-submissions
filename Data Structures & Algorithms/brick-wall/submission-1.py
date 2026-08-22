from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)

        for row in wall:
            pos = 0

            for brick in row[:-1]:
                pos += brick
                edges[pos] += 1

        max_edges = max(edges.values(), default=0)

        return len(wall) - max_edges