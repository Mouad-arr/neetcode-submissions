def atMost(nums, goal):
    if goal < 0:
        return 0

    left = 0
    s = 0
    res = 0

    for right in range(len(nums)):
        s += nums[right]

        while s > goal:
            s -= nums[left]
            left += 1

        res += right - left + 1

    return res


class Solution:
    def numSubarraysWithSum(self, nums, goal):
        return atMost(nums, goal) - atMost(nums, goal - 1)   