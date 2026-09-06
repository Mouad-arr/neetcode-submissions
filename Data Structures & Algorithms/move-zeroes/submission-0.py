class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,n=0,len(nums)
        while i<n :
            if nums[i]==0:
                j=i+1
                k=i
                while j<n:
                    if nums[j]!=0:
                        nums[k],nums[j]=nums[j],nums[k]
                        k=j
                        j+=1
                    else :
                        j+=1
                n-=1
            i+=1
            
        