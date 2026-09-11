class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        left,right=0,n-1
        count=0
        MOD = 10**9 + 7
        while right >= 0:
            if left <= right and nums[left]+nums[right]<=target:
                if left==right:
                    count+=1
                else:
                    count+= pow(2,right-left-1)
                left+=1
            else:
                left=0
                right-=1
        count %= MOD
        return count