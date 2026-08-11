class Solution:
    def check(self, nums: List[int]) -> bool:
        checked=False
        for i in range(len(nums)-1) :
            if nums[i]>nums[i+1]:
                if checked :
                    return False
                checked=True
        if checked and nums[-1]>nums[0]:
            return False
        return True