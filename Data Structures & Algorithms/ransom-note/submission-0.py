class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote) :
            return False
        mp={}
        for c in magazine :
            if c in mp:
                mp[c]+=1
            else :
                mp[c]=1
        for c in ransomNote :
            if c not in mp:
                return False
            if ransomNote.count(c)>mp[c]:
                return False
        return True