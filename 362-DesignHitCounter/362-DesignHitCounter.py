# Last updated: 4/2/2025, 2:12:29 AM
from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        res = 0
        while self.queue:
            diff = timestamp - self.queue[0] # 301 -1 = 300
            if diff>= 300:
                self.queue.popleft()
            else:
                break

        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)