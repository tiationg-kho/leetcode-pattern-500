from heapq import *
class ListNode:
    def __init__(self, id=- 1, timestamp=- 1, next=None):
        self.id = id
        self.timestamp = timestamp
        self.next = next

class Twitter:

    def __init__(self):
        self.id_tweets = defaultdict(ListNode)
        self.timestamp = 0
        self.id_follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.id_tweets[userId]
        self.id_tweets[userId] = ListNode(tweetId, self.timestamp, tweets)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        nodes = [self.id_tweets[userId]]
        for id in self.id_follows[userId]:
            nodes.append(self.id_tweets[id])
        heap = []
        for i, node in enumerate(nodes):
            if node.id != - 1:
                heap.append((- node.timestamp, i))
        heapify(heap)
        res = []
        while len(res) < 10 and heap:
            _, i = heappop(heap)
            res.append(nodes[i].id)
            nodes[i] = nodes[i].next
            if nodes[i].id != - 1:
                heappush(heap, (- nodes[i].timestamp, i))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.id_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.id_follows[followerId]:
            self.id_follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# time O(k + 10logk) for getNewsFeed(), others are O(1)
# space O(n), n is total tweets
# using heap and k way merge problem and hashmap