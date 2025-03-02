class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        self.arr.append(val)
        self.seen[val]= len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        idx = self.seen.get(val)
        last = len(self.arr)-1
        lastItem = self.arr[last]
        self.seen[lastItem] = idx
        self.seen.pop(val)
        self.arr[idx],self.arr[last] = self.arr[last],self.arr[idx]
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()