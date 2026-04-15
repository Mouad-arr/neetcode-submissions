class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        for i in range(n):
            cur=0
            for j in range(i,n):
                cur+=nums[j]
                res=max(res,cur)
        return res
        # def dfs(i,s):
        #     if (i,s) in visited:
        #         return visited[(i,s)]+s
        #     s+=nums[i]
        #     if i == n-1 :
        #         visited[(i,s)]=s
        #         return s
        #     m=-float('inf')
        #     for j in range(i+1,n):
        #         m=max(m,dfs(j,s),dfs(j,0))
        #     visited[(i,s)]=m
        #     return m
        