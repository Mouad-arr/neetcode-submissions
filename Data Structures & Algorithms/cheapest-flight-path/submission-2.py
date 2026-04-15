from collections import defaultdict, deque
import math

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        q = deque([(src, 0)])  # (city, cost)
        stops = 0
        dist = [math.inf] * n
        dist[src] = 0

        while q and stops <= k:
            for _ in range(len(q)):
                city, cost = q.popleft()
                for nei, price in graph[city]:
                    if cost + price < dist[nei]:
                        dist[nei] = cost + price
                        q.append((nei, cost + price))
            stops += 1

        return -1 if dist[dst] == math.inf else dist[dst]
