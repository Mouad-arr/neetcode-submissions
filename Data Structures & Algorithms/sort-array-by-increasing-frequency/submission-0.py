class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp={}
        for num in nums:
            if num in mp:
                mp[num]+=1
            else :
                mp[num]=1
        items = sorted(mp.items(), key=lambda x: x[0], reverse=True)
        items = sorted(items, key=lambda x: x[1])

        sorted_mp = dict(items)
        res=[]
        for num in sorted_mp:
            res+=[num]*sorted_mp[num]
        return res