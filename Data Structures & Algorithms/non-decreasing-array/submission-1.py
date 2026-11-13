class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        i=1
        changed=False
        mx=-float('INF')
        while i<n :
            if nums[i-1]>nums[i]:
                if not changed :
                    temp=nums[i-1]
                    nums[i-1]=nums[i]
                    if nums[i-1]<mx :
                        nums[i]=temp
                        nums[i-1]=temp
                    changed=True
                else :
                    return False
            mx=max(mx,nums[i-1])
            i+=1
        return True
