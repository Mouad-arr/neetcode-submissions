class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        def dfs(i):
            if i==n-1 :  
                return True
            else:
                m=nums[i]
                if m==0:
                    return False
                else :
                    for j in range(1,m+1):
                        if i+j < n and dfs(i+j):
                            return True
                return False
        return dfs(0)