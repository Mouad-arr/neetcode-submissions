class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pair = False
        if nums[0]%2==0:
            pair = True
        for i in range(1,len(nums)):
            if pair and nums[i]%2==0:
                return False
            elif not pair and nums[i]%2!=0:
                return False
            pair=not pair
        return True