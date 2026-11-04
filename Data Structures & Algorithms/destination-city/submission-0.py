class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fro=set(path[0] for path in paths)
        for path in paths :
            if path[1] not in fro:
                return path[1]
        return ""
