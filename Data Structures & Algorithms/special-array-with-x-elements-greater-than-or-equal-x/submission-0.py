class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        x=1
        i=len(nums)-1
        while i>=0:
            if i-1 >=0 and nums[i]>=x and nums[i-1]<x :
                return x 
            elif i-1<0 and nums[i]>=x:
                return x
            else:
                x+=1
            i-=1
        return -1