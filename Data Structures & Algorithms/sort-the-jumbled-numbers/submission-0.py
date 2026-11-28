class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n=len(nums)
        mp={}
        mapped_nums=[0]*n
        count={}
        for i in range(n):
            r=""
            m=len(str(nums[i]))
            num=nums[i]
            while m >0 :
                x=10**(m-1)
                y=num//x
                num%=x
                r+=str(mapping[y])
                m-=1
            mapped_nums[i]=int(r)
            mp[nums[i]]=int(r)
            count[nums[i]] = count.get(nums[i], 0) + 1
        sorted_mp=dict(sorted(mp.items(),key=lambda x : x[1]))
        res=[0]*n
        i=0
        for k in sorted_mp.keys():
            for j in range(count[k]):
                res[i]=k
                i+=1
        return res

