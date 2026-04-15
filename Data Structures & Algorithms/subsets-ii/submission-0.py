class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def dfs(i,current) :
            if i == len(nums) :
                res.add(tuple(sorted(current)))
                return
            res.add(tuple(sorted(current)))
            current.append(nums[i])
            dfs(i+1,current)
            current.pop()
            dfs(i+1,current)
        dfs(0,[])
        return [list(t) for t in res]