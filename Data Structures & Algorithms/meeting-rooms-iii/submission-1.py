class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        dic={}
        for i in range(n):
            dic[i]=[0,0]
        time=0
        j=0
        k=len(meetings)
        while j<k :
            meet=meetings[j]
            m=float('inf')
            good=False
            for i in dic :
                m=min(m,dic[i][1])
                if meet[0] >= dic[i][1]:
                    dic[i][1]=meet[1]
                    dic[i][0]+=1
                    j+=1
                    good=True
                    break
                elif meet[0] <= time and time >= dic[i][1]:
                    dic[i][0]+=1
                    dic[i][1]+=( meet[1]-meet[0] )
                    j+=1
                    good=True
                    break
            if not good :
                time = m
        m=0
        res=-1
        for i in dic :
            if m < dic[i][0]:
                res=i
                m=dic[i][0]
        return res
            
                