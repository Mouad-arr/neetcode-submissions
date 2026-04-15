class TrieNode :
    def __init__(self):
        self.children={}
        self.endOfWord=False
class Solution:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children :
                cur.children[c] = TrieNode()
            cur=cur.children[c]
        cur.endOfWord = True 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        ROW,COLS=len(board),len(board[0])
        res,visit = set(),set()
        def dfs(r,c,node,wordSoFar) :
            if r<0 or c<0 or r>=ROW or c >= COLS or (r,c) in visit or board[r][c] not in node.children :
                return 
            visit.add((r, c))
            node = node.children[board[r][c]]
            wordSoFar += board[r][c]
            if node.endOfWord :
                res.add(wordSoFar)
            dfs(r+1,c,node,wordSoFar)
            dfs(r-1,c,node,wordSoFar)
            dfs(r,c+1,node,wordSoFar)
            dfs(r,c-1,node,wordSoFar)
            visit.remove((r,c))
        for r in range(ROW):
            for c in range(COLS):
                dfs(r,c,self.root,"")
        return list(res)