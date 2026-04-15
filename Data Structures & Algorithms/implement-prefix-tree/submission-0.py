class PrefixTree:

    def __init__(self):
        self.prefixTree = []
    def insert(self, word: str) -> None:
        self.prefixTree.append(word)

    def search(self, word: str) -> bool:
        return  word in self.prefixTree 

    def startsWith(self, prefix: str) -> bool:
        for word in self.prefixTree :
            if len(prefix)<=len(word) :
                if list(prefix) == list(word)[:len(prefix)] :
                    return True
        return False
        