class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p

        if r == 0:
            return 0
            
        mp = {0: -1}

        prefix = 0
        ans = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - r) % p

            if needed in mp:
                ans = min(ans, i - mp[needed])

            mp[prefix] = i

        return ans if ans < len(nums) else -1
        