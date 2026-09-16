class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=n-1
        m=0
        while i>=0:
            cur = 1
            j=i-1
            c=0
            while j>=0 :
                if nums[i] - nums[j] <= k-c:
                    c+=nums[i]-nums[j]
                    cur+=1
                    j-=1
                else:
                    break
            m=max(m,cur)
            i-=1
        return m