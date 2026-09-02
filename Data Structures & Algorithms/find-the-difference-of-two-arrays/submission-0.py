class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[[],[]]
        for num in set(nums1):
            if num not in set(nums2):
                answer[0].append(num)
        for num in set(nums2):
            if num not in set(nums1):
                answer[1].append(num)
        return answer