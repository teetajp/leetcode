from collections import defaultdict, deque
import heapq

class Twitter:
    # number of tweets >> number of users and followers

    def __init__(self):
        self.newsfeeds = defaultdict(list) # key: userID, value: maxheap based on tweetID
        self.tweets =  defaultdict(deque) # key: userID, value: list of 10 most recent tweets
        self.max_feed_len = 10
        self.followers = defaultdict(set)
        self.followees = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        
        if len(self.tweets[userId]) > self.max_feed_len:
            # remove oldest tweet if user tweeted has more than 10 tweets
            self.tweets[userId].popleft()
        
        if userId not in self.followers[userId]:
            # add "self" as subscriber to own tweets
            self.followers[userId].add(userId)
            self.followees[userId].add(userId)
        
        # Update users' newsfeeds?
        for follower in self.followers[userId]:
            heapq.heappush(self.newsfeeds[follower], (-self.time, tweetId, userId))
        
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res_tweetTimes = []
        res_tweetIds = []
        res_tweetUserIds = []
        
        while len(res_tweetIds) < self.max_feed_len and self.newsfeeds[userId]:
            tweetTime, tweetId, followeeId = heapq.heappop(self.newsfeeds[userId])
            
            if followeeId in self.followees[userId]:
                # only display tweets from those the user is following
                res_tweetTimes.append(tweetTime)
                res_tweetIds.append(tweetId)
                res_tweetUserIds.append(followeeId)
        
        # reinsert tweets back into heap
        for tweetTime, tweetId, followeeId in zip(res_tweetTimes,
                                                  res_tweetIds,
                                                  res_tweetUserIds):
            heapq.heappush(self.newsfeeds[userId], (tweetTime, tweetId, followeeId))
                
        return res_tweetIds

    def follow(self, followerId: int, followeeId: int) -> None:
        # max newsfeed heap size: len(following) * 10 <= 500 * 10
        if followeeId in self.followees[followerId] or followerId == followeeId:
            return

        for tweetTime, tweetId in self.tweets[followeeId]:
            heapq.heappush(self.newsfeeds[followerId], (tweetTime, tweetId, followeeId))
            
        self.followers[followeeId].add(followerId)
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followees[followerId] or followerId == followeeId:
            return
        
        # could filter and reheapify newsfeed here OR leave it to the newsfeed method
        # XXX: if user unsubs before get newsfeed, then filtering and reheapify might be unnecessary work
        self.followers[followeeId].remove(followerId)
        self.followees[followerId].remove(followeeId)
        
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)