from collections import defaultdict


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user2tweet = defaultdict(list)
        self.user2user = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.follow(userId, userId)
        self.user2tweet[userId].append((self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res, temp = [], []
        idx = defaultdict(lambda: -2)
        for i in self.user2user[userId]:
            try:
                temp.append(self.user2tweet[i][-1])
            except IndexError:
                pass
        while temp and len(res) < 10:
            temp.sort()
            t, tweet, user = temp.pop()
            res.append(tweet)
            try:
                temp.append(self.user2tweet[user][idx[user]])
                idx[user] -= 1
            except IndexError:
                pass
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.user2user[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        try:
            self.user2user[followerId].remove(followeeId)
        except KeyError:
            pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
