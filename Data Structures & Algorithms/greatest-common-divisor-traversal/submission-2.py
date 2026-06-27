class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)
        mp={}
        for i in range(n-1):
            if nums[i]==1 :
                return False
            if nums[i] not in mp:
                mp[nums[i]]=set()
            for j in range(i+1,n):
                if math.gcd(nums[i],nums[j])>1 :
                    mp[nums[i]].add(nums[j])
                    if nums[j] not in mp:
                        mp[nums[j]]={nums[i]}
                    else:
                        mp[nums[j]].add(nums[i])
        visited=set()
        def dfs(num) :
            visited.add(num)
            for nu in mp[num] :
                if nu not in visited :
                    dfs(nu)
        dfs(nums[0])
        return len(visited)==len(set(nums)) 