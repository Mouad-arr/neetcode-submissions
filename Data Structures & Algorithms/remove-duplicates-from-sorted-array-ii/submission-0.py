class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=n-1
        end=n-1
        while i>=0 :
            if i-1 >= 0 and nums[i]==nums[i-1]:
                if i-2 >= 0 and nums[i]==nums[i-2]:
                    j=i-2
                    while j>=0 and nums[j]==nums[i]:
                        j-=1
                    k=i+1
                    while k<=end:
                        nums[k-i+j+2]=nums[k]
                        k+=1
                    end-=(i-j-2)
                    i=j
                else :
                    i-=2
            else:
                i-=1
        return end+1