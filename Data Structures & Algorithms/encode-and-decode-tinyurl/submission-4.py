class Solution:
    def __init__(self):
        self.mp = {}
        self.code = 0

    def encode(self, longUrl: str) -> str:
        self.code += 1
        shortUrl = str(self.code)
        self.mp[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.mp[shortUrl]