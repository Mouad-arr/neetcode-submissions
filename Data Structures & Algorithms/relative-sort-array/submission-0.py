class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for e in arr2 :
            res += [e]*arr1.count(e)
        ans=[]
        for e in arr1:
            if e not in arr2:
                ans.append(e)
        ans.sort()
        res+=ans
        return res