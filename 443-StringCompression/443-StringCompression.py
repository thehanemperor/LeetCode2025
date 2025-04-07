# Last updated: 4/7/2025, 3:23:26 AM
from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if not self.queue or self.queue[-1][0] != timestamp:
            self.queue.append((timestamp,1))
        else:
            lastTimestamp, count = self.queue[-1]
            self.queue.pop()
            self.queue.append((timestamp,count+1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        while self.queue:
            diff = timestamp - self.queue[0][0] # 301 -1 = 300
            if diff>= 300:
                oldTimestamp,oldCount = self.queue.popleft()
                self.total -= oldCount
            else:
                break

        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)