class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (j-i) <= k :
                    return True
        return False