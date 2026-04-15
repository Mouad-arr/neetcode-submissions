class Solution:
    def checkValidString(self, s: str) -> bool:
        storage={}
        def dfs(i, open):
            if (i,open) in storage:
                return storage[(i,open)]
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == '(':
                storage[(i,open)]= dfs(i + 1, open + 1)
            elif s[i] == ')':
                storage[(i,open)]=  dfs(i + 1, open - 1)
            else:
                storage[(i,open)]=  (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
            return storage[(i,open)]
        return dfs(0, 0)