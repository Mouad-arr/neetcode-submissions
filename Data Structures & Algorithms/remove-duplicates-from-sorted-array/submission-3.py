class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,k=0,0
        n=len(nums)
        if n==1 :
            return n
        res=[]
        while i<n-1:
            while i<n-1 and nums[i]==nums[i+1]:
                i+=1
            res.append(nums[i])
            i+=1
            k+=1
        if i==n-1 and nums[i-1]!=nums[i]:
            res.append(nums[i])
            k+=1
        for i in range(k):
            nums[i]=res[i]
        return k