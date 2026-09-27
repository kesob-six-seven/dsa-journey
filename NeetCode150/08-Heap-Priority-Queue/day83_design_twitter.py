"""
Day 83 — NeetCode 150: Heap / Priority Queue
Design Twitter (LC 355) — Medium
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
    Each user has a tweet list and a follow set. getFeed merges the 10
    most recent tweets across all followed users using a max heap on
    timestamp — same pattern as Merge K Sorted Lists.
    """

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)   # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set) # userId -> {followeeId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1  # decrement so heap acts as max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        # include own tweets
        sources = list(self.following[userId]) + [userId]

        heap = []
        for uid in sources:
            tweets = self.tweets[uid]
            if tweets:
                # push (timestamp, tweetId, userTweets, index)
                idx = len(tweets) - 1
                heapq.heappush(heap, (tweets[idx][0], tweets[idx][1], tweets, idx))

        while heap and len(feed) < 10:
            ts, tweetId, tweets, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                heapq.heappush(heap, (tweets[idx-1][0], tweets[idx-1][1], tweets, idx-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)