class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,n=0,len(nums)
        k=k%n
        for i in range(k):
            temp=nums[-1]
            for i in range(n-2,-1,-1):
                nums[i+1]=nums[i]
            nums[0]=temp

