class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mp = {}
        for i in range(n):
            mp.setdefault(manager[i], []).append(i)
        q=deque([(headID,0)])
        mx=0
        while len(q)!= 0:
            m=len(q)
            for _ in range(m):
                (head,time)=q.popleft()
                if head not in mp:
                    mx=max(mx,time)
                else:
                    for emp in mp[head]:
                        q.append((emp,time+informTime[head]))
        return mx
