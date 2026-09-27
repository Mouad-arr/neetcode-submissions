class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        while left <= right :
            mid = (left+right)//2
            if mid > 0 and nums[mid-1]==nums[mid]:
                if (mid-1)%2==0:
                    left=mid+1
                else:
                    right=mid-2
            elif mid<n-1 and nums[mid+1]==nums[mid]:
                if mid%2 == 0:
                    left=mid+2
                else:
                    right=mid-1
            else:
                return nums[mid]
        return nums[left]