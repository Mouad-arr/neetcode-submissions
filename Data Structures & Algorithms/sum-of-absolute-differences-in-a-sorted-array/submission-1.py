class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        i=1
        s=0
        while i<n:
            s+=(nums[i]-nums[0])
            i+=1
        res.append(s)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                res.append(res[-1])
            else:
                res.append(res[-1]+(nums[i]-nums[i-1])*(2*i-n))
        return res