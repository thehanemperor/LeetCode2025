# Last updated: 4/1/2025, 4:13:35 PM
class RandomizedCollection:

    def __init__(self):
        self.stack = []
        self.stackIndex = defaultdict(set)

    def insert(self, val: int) -> bool:
            self.stack.append(val)
            self.stackIndex[val].add(len(self.stack)-1)
            return len(self.stackIndex[val]) == 1 # because of empty set
        

    def remove(self, val: int) -> bool:
        if val not in self.stackIndex or not self.stackIndex[val]:
            return False
        last = self.stack[-1]
        valIndex = self.stackIndex[val].pop()
        self.stack[valIndex] = last
        self.stackIndex[last].add(valIndex)
        self.stackIndex[last].remove(len(self.stack)-1) #only remove one element
        self.stack.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()