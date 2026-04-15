class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(i,flag):
            if i==n:
                if flag:
                    return 0
                return -1e6
            if flag:
                return max(0,nums[i]+dfs(i+1,True))
            else :
               return max(dfs(i+1,False),nums[i]+dfs(i+1,True)) 
        return dfs(0,False)