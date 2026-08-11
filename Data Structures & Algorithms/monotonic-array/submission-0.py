class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1 :
            return True
        asc=True
        if nums[0]>nums[1]:
            asc=False
        for i in range(1,n-1):
            if asc and nums[i]>nums[i+1]:
                return False
            elif not asc and nums[i]<nums[i+1]:
                return False
        return True