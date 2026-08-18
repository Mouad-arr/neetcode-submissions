class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp={}
        for i in range(len(names)):
            mp[heights[i]]=names[i]
        heights.sort(reverse=True)
        res=[]
        for h in heights:
            res.append(mp[h])
        return res