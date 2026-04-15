class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        def dfs(index):
            if index <0:
                return
            val=nums[index]
            if val in d:
                i=index+1
                while nums[i]!=val:
                    if val < nums[i]:
                        d[val]=max(d[nums[i]]+1,d[val])
                    i+=1
                dfs(index-1)
                return
            count=0
            for i in range(index+1,n):
                if val < nums[i]:
                    count=max(count,d[nums[i]])
            d[val]=count+1
            dfs(index-1)
        dfs(n-1)
        return max([x for x in d.values()])