class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=1
        sup=True
        while i<n:
            if sup and nums[i] < nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            elif not sup and nums[i-1]<nums[i]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            sup=not sup
            i+=1
