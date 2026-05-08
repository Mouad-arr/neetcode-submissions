class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        if n==1 :
            return n
        res=[]
        while i<n-1:
            while i<n-1 and nums[i]==nums[i+1]:
                i+=1
            res.append(nums[i])
            i+=1
        if i==n-1 and nums[i-1]!=nums[i]:
            res.append(nums[i])
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)