class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)
        if n%2 !=0:
            return False
        for e in set(nums):
            if nums.count(e) % 2 !=0 :
                return False
        return True