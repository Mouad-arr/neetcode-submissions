class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d=defaultdict(list)
        for T in tickets :
            d[T[0]].append(T[1])
        res=[]
        def dfs(edge):
            if edge not in d:
                res.append(edge)
                return
            d[edge].sort(reverse=True)
            while d[edge] :
                e=d[edge].pop()
                dfs(e)
            res.append(edge)
        dfs("JFK")
        return res[::-1]