class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        def dfs(i):
            if i in d :
                return d[i]
            res=float('inf')
            if i>= n :
                return +float('inf')
            if i==n-1 :
                return 0
            for j in range(1,nums[i]+1) :
                x=dfs(i+j)+1
                if x < float('inf') :
                    res=min(res,x)
            d[i]=res
            return res
        return dfs(0)