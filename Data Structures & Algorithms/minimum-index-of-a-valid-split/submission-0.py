class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        dominant=-1
        for num in set(nums):
            x=nums.count(num)
            if x > n/2:
                dominant = num
        if dominant == -1 :
            return -1
        i=0
        while i<n-1 :
            if nums[:i+1].count(dominant) > len(nums[:i+1])/2 and nums[i+1:].count(dominant) > len(nums[i+1:])/2 :
                return i
            i+=1
        return -1