class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize=1
        dp={}
        def dfs(i) :
            if arr[i]==arr[i+1]:
                return 1
            elif arr[i]>arr[i+1] :
                return 2 + fun(i+1,False)
            else:
                return 2 + fun(i+1,True)
        def fun(i,Greater):
            if (i,Greater) in dp:
                return dp[(i,Greater)]
            res=0
            if i==len(arr)-1 :
                return res
            elif Greater and  arr[i]>arr[i+1] :
                res= 1+fun(i+1,False)
            elif not Greater and arr[i]<arr[i+1] :
                res= 1+fun(i+1,True)
            dp[(i,Greater)]=res
            return res
        for i in range(len(arr)-1):
            maxSize=max(maxSize,dfs(i))
        return maxSize