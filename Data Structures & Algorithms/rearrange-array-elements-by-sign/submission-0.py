class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        positives=[0]*(n//2)
        negatives=[0]*(n//2)
        i,j=0,0
        for num in nums :
            if num>0:
                positives[i]=num
                i+=1
            else:
                negatives[j]=num
                j+=1
        i,j=0,0
        for k in range(n):
            if k%2==0 :
                nums[k]=positives[i]
                i+=1
            else:
                nums[k]=negatives[j]
                j+=1
        return nums