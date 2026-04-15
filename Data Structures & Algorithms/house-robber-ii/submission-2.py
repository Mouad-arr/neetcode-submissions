class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 :
            return nums[0]
        elif n==2:
            return max(nums[1],nums[0])
        memo1=[-1]*(n-1)
        memo2=[-1]*(n-1)
        nums1=nums[:n-1]
        nums2=nums[1:]
        def dfs1(i):
            if i>=len(nums1):
                return 0
            if memo1[i]!=-1 :
                return memo1[i]
            memo1[i]=max(dfs1(i+1),nums1[i]+dfs1(i+2))
            return memo1[i]
        def dfs2(i):
            if i>=len(nums2):
                return 0
            if memo2[i]!=-1 :
                return memo2[i]
            memo2[i]=max(dfs2(i+1),nums2[i]+dfs2(i+2))
            return memo2[i]
        
        return max(dfs1(0),dfs2(0))