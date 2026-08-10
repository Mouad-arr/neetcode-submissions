class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largest=-1
        for i in set(arr) :
            if i==arr.count(i):
                largest=max(largest,i)
        return largest