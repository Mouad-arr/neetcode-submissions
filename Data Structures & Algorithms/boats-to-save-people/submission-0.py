class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        n=len(people)
        people.sort()
        left,right= 0 , n-1
        while left  < right :
            if people[left]+people[right] <= limit :
                res+=1
                left+=1
                right-=1
            else :
                res+=1
                right-=1
        if left==right :
            res+=1
        return res