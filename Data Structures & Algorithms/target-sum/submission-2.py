class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        d={}
        def dfs(i, cur):
            if (i,cur) in d:
                return d[(i,cur)]
            elif i==n-1 and cur != target:
                return 0
            elif i==n-1 and cur == target :
                return 1
            else:
                d[ (i,cur) ] = dfs(i+1, cur + nums[i+1]) + dfs(i+1, cur - nums[i+1])
                return d[(i,cur)]
        return dfs(0,-nums[0])+dfs(0,nums[0])