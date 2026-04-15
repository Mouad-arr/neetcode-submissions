class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        d={}
        def dfs(i, sign , s):
            if (i,sign,s) in d:
                return d[(i,sign,s)]
            if sign=='+' :
                if i==n-1 and s+nums[i] !=target:
                    return 0
                elif i==n-1 and s+nums[i] ==target :
                    return 1
                else:
                    d[(i,sign,s)]=dfs(i+1,"+",s+nums[i]) + dfs(i+1,'-',s+nums[i])
                    return d[(i,sign,s)]
            else:
                if i==n-1 and s-nums[i] !=target:
                    return 0
                elif i==n-1 and s-nums[i] ==target :
                    return 1
                else:
                    d[(i,sign,s)]=dfs(i+1,"+",s-nums[i]) + dfs(i+1,'-',s-nums[i])
                    return d[(i,sign,s)]
        return dfs(0,'+',0)+dfs(0,'-',0)