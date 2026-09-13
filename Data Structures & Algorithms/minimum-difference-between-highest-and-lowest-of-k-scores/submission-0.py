class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j=1,k
        n=len(nums)
        res=nums[k-1]-nums[0]
        while j<n:
            res=min(res,nums[j]-nums[i])
            i+=1
            j+=1
        return res