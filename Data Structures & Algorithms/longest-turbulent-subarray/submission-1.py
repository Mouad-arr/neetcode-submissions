class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize=1
        def dfs(i) :
            if arr[i]==arr[i+1]:
                return 1
            elif arr[i]>arr[i+1] :
                return 2 + fun(i+1,False)
            else:
                return 2 + fun(i+1,True)
        def fun(i,Greater):
            if i==len(arr)-1 :
                return 0
            elif Greater and  arr[i]>arr[i+1] :
                return 1+fun(i+1,False)
            elif not Greater and arr[i]<arr[i+1] :
                return 1+fun(i+1,True)
            return 0
        for i in range(len(arr)-1):
            maxSize=max(maxSize,dfs(i))
        return maxSize