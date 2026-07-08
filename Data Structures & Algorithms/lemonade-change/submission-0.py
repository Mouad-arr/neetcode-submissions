class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        mp={
            5:1,
            10:0,
        }
        for i in range(1,len(bills)) : 
            if bills[i]==5 :
                mp[5]+=1
            elif bills[i]==10 :
                if mp[5]>0 :
                    mp[5]-=1
                    mp[10]+=1
                else :
                    return False
            else :
                if mp[10]>0 and mp[5]>0 :
                    mp[10]-=1
                    mp[5]-=1
                elif mp[5]>2 :
                    mp[5]-=3
                else:
                    return False
        return True