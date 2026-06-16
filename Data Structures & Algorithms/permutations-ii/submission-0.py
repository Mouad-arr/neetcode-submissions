class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        def dfs(cur) :
            if len(cur)==n :
                res.add(tuple(cur))
                return
            for j in range(n) :
                if nums[j] != float("-inf"):
                    cur.append(nums[j])
                    nums[j] = float("-inf")
                    dfs(cur)
                    nums[j]=cur[-1]
                    cur.pop()
        dfs([])
        return list(res)