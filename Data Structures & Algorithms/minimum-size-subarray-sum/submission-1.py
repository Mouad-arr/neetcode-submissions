class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        res=[]
        for i in range(n):
            x=nums[i]
            if x>=target:
                res.append(1)
                continue
            for j in range(i+1,n):
                x+=nums[j]
                if x>= target :
                    res.append(j-i+1)
                    break
        if len(res)==0:
            return 0
        else :
            return min(res)