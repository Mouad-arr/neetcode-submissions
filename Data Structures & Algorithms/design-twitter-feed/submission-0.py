class Twitter:

    def __init__(self):
        self.time=0
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        L=self.tweetMap[userId][:]
        for followId in self.followMap[userId]:
            L.extend(self.tweetMap[followId])
        L.sort(key = lambda x : x[0], reverse=True)
        return [tweetId for _,tweetId in L[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId : 
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)