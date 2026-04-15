class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0
        D=defaultdict(set)
        def isTrue(word,W):
            diff = 0
            for i in range(len(word)):
                if word[i] != W[i]:
                    diff += 1
            return diff == 1
        for word in wordList :
            if isTrue(word,beginWord):
                D[beginWord].add(word)
        for W in wordList:
            for word in wordList:
                if word==W :
                    continue
                if isTrue(word,W):
                    D[W].add(word)
        q = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            curr, dist = q.popleft()
            if curr == endWord:
                return dist
            for neighbor in D[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
        return 0