class User:
    def __init__(self, id):
        self.id = id
        self.tweets = []
        self.followers = set()
        self.following = set()

class Tweet:
    def __init__(self, id, cnt, userId):
        self.id = id
        self.cnt = cnt
        self.userId = userId


class Twitter:
    """
    """
    # user:
    # id
    # tweets
    # followers
    # following
    # cant rly keep a store of feed tweets, in the case user unfollows smo
    # no way to efficiently remove said tweets 
    # 10 most = k most (heap problem?)
    def __init__(self):
        # users
        self.users = dict()
        # tweets -> cnt ascending
        # self.tweets = smth
        self.tweetCount = 0
        
    def createUserIfNot(self, uid):
        if uid not in self.users:
            self.users[uid] = User(uid)



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUserIfNot(userId)
        
        self.users[userId].tweets.append(Tweet(tweetId, self.tweetCount, userId))
        self.tweetCount += 1
        return None

        
    # heap 
    # merge k sorted lists type approach 
    def getNewsFeed(self, userId: int) -> List[int]:
        print("call")
        maxHeap = []
        res = []
        allUsers = [self.users[userId]]
        for uid in self.users[userId].following:
            allUsers.append(self.users[uid])
        
        ctr = 0
        for user in allUsers:
            if user.tweets:
                heapq.heappush(maxHeap, (-user.tweets[-1].cnt, ctr, user.tweets[-1], -1))
            ctr += 1
        
        while maxHeap and len(res) < 10:
            _, _, twt, idx = heapq.heappop(maxHeap)
            res.append(twt.id)
            twtUser = self.users[twt.userId]
            if len(twtUser.tweets) > -idx:
                newIdx = idx - 1
                heapq.heappush(maxHeap, (-twtUser.tweets[newIdx].cnt, ctr, twtUser.tweets[newIdx], newIdx))
                ctr +=1


        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        self.createUserIfNot(followerId)
        self.createUserIfNot(followeeId)
        self.users[followerId].following.add(followeeId)
        self.users[followeeId].followers.add(followerId)
        return None
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        self.createUserIfNot(followerId)
        self.createUserIfNot(followeeId)
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
        if followerId in self.users[followeeId].followers:
            self.users[followeeId].followers.remove(followerId)
        return None

        
