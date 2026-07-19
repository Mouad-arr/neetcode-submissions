class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1  :
            return 1
        dic={}
        for i in range(1,n+1):
            dic[i]=set()
        for tr in trust :
            dic[tr[0]].add(tr[1])
        trusted=-1
        for p in dic :
            if len(dic[p])==0 :
                if trusted ==-1 :
                    trusted=p
                else :
                    return -1
        for p in dic :
            if trusted!=p and trusted not in dic[p] :
                return -1
        return trusted