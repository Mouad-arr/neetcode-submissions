class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        i=0
        while i<n:
            k=1
            while i+1<n and nums[i+1]==nums[i]:
                k+=1
                i+=1
            m=len(res)
            for j in range(min(k,m)):
                res[j].append(nums[i])
            if k>m:
                for j in range(k-m):
                    res.append([nums[i]])
            i+=1
        return res


