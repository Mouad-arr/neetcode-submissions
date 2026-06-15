class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur):
            if len(cur)==k:
                res.append(list(cur))
                return
            cur.add(i)
            if i+1> n:
                if len(cur)==k:
                    res.append(list(cur))
                cur.remove(i)
                return
            dfs(i+1,cur)
            cur.remove(i)
            dfs(i+1,cur)
        dfs(1,set())
        return res
