class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            maxIdx = 0
            for i in range(1, len(gifts)):
                if gifts[i] > gifts[maxIdx]:
                    maxIdx = i
            gifts[maxIdx] = int(sqrt(gifts[maxIdx]))
        return sum(gifts)