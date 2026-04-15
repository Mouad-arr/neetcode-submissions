class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 :
            return nums[0]
        res=0
        for i in range(n):
            curr=1
            j=i
            while j<n:
                curr*=nums[j]
                res=max(res,curr)
                j+=1
        return res

            
