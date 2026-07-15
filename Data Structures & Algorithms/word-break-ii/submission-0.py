class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        wordSet = set(wordDict)
        def dfs(i, cur):
            if i == len(s):
                res.append(" ".join(cur))
                return

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordSet:
                    cur.append(word)
                    dfs(j, cur)
                    cur.pop()
        dfs(0,[])
        return res