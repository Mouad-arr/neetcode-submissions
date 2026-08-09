class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n=len(arr)
        i=0
        count=0

        while i<n and count < k :
            if arr.count(arr[i])==1 :
                count+=1
            i+=1
        if count ==k:
            return arr[i-1]
        else:
            return ""