class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vector = [v1,v2]
        self.queue = deque()
        for i in range(len(self.vector)):
            if len(self.vector[i])>0:
                self.queue.append((i,0))


    def next(self) -> int:
        vdex,index = self.queue.popleft()
        if index+1 < len(self.vector[vdex]):
            self.queue.append((vdex, index+1))

        return self.vector[vdex][index]

    def hasNext(self) -> bool:
        return len(self.queue) >0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())