class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S=sum(nums)
        n=len(nums)
        if S%2!=0:
            return False
        visited=set()
        def dfs(index,s):
            visited.add(index)
            if nums[index]+s == S//2:
                return S//2
            if nums[index]+s > S//2:
                visited.remove(index)
                return s
            cur=0
            i=index+1
            while i < n and cur!=S//2:
                cur=dfs(i,s+nums[index])
                i+=1
            if cur==S//2:
                return S//2
            else:
                visited.remove(index)
                return s
        if dfs(0,0)==S//2:
            for i in range(n):
                if i not in visited:
                    index=i
                    break
            return  dfs(index,0)==S//2
        return False