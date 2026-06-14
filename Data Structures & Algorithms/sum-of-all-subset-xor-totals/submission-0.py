class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        def dfs(index,subset):
            nonlocal s
            xorr=0
            for num in subset :
                xorr^=num
            s+=xorr
            for j in range(index,n):
                subset.append(nums[j])
                dfs(j+1,subset)
                subset.pop()
        dfs(0,[])
        return s
            