"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        isLeaf=True
        for i in range(n-1) :
            for j in range(n-1):
                if grid[i][j]==grid[i+1][j] and grid[i][j]==grid[i][j+1] :
                    continue
                else :
                    isLeaf=False
                    break
            if not isLeaf :
                break
        if isLeaf :
            return Node(grid[0][0],1,None,None,None,None)
        else:
            topLeft = [row[:n//2] for row in grid[:n//2]]
            topRight = [row[n//2:] for row in grid[:n//2]]
            bottomLeft = [row[:n//2] for row in grid[n//2:]]
            bottomRight = [row[n//2:] for row in grid[n//2:]]
            return Node(0,0, self.construct(topLeft),
                    self.construct(topRight),
                    self.construct(bottomLeft),
                    self.construct(bottomRight))