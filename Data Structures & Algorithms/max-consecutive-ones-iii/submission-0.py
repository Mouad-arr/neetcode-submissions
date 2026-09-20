class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        credits=0
        n=len(nums)
        i,j=0,0
        res=0
        count=0
        while i<n :
            if j<n and nums[j]==1:
                count+=1
                j+=1
                continue
            if j<n and nums[j]==0:
                if credits<k :
                    count+=1
                    j+=1
                    credits+=1
                else :
                    res=max(res,count)
                    while i<n and nums[i]==1:
                        count-=1
                        i+=1
                    i+=1
                    if i<n :
                        j+=1
                    else :
                        return res
                continue
            break
        res=max(count,res)
        return res



                        