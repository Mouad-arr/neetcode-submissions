class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mp={}
        for c in chars :
            if c in mp :
                mp[c]+=1
            else :
                mp[c]=1
        length=0
        good=True
        for word in words :
            good = True
            for i in range(len(word)):
                if word[i] not in mp:
                    good = False
                    break
                else:
                    if word.count(word[i]) > mp[word[i]]:
                        good=False
                        break   
            if good :
                length+=len(word)
        return length