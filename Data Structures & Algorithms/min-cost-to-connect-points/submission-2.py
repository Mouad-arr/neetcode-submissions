class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1,p2) :
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) 
        d=defaultdict(list)
        n=len(points)
        for i in range(n-1) :
            for j in range(i+1,n) :
                d[distance(points[i],points[j])].append((i,j))
        connected=[]
        d_trie_key = dict(sorted(d.items(), key=lambda item: item[0]))  
        res=0
        i=0
        con=False
        for key in d_trie_key.keys():
            for val in d_trie_key[key]:
                con=False
                setOf0=-1
                setOf1=-1
                index=0
                for s in connected :
                    if val[0] in s and val[1] in s:
                        con=True
                        break
                    elif val[0] in s :
                        setOf0=index
                    elif val[1] in s :
                        setOf1=index
                    index+=1  
                if con :
                    continue
                if setOf0 == setOf1== -1 :
                    res+=key
                    i+=1
                    connected.append({val[0],val[1]})
                elif setOf0 == -1:
                    connected[setOf1].add(val[0])
                    res+=key
                    i+=1
                elif setOf1 == -1:
                    connected[setOf0].add(val[1])
                    res+=key
                    i+=1
                else:
                    connected[setOf0].update(connected[setOf1]) 
                    connected.pop(setOf1)
                    res+=key
                    i+=1
                if i==n-1:
                    break
            if i==n-1 :
                break
        return res