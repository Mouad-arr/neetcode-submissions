from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        sorted_items = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result