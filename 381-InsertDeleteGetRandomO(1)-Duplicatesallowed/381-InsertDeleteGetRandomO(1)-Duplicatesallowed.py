# Last updated: 4/1/2025, 2:50:28 PM
class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.stackIndex= {}

    def insert(self, val: int) -> bool:
        if val in self.stackIndex:
            return False
        self.stack.append(val)
        self.stackIndex[val] = len(self.stack)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.stackIndex:
            return False
        index = self.stackIndex[val]
        last = len(self.stack)-1
        switch = self.stack[last]
        self.stack[index],self.stack[last] = self.stack[last],self.stack[index]
        
        self.stackIndex[switch] = index
        self.stack.pop()
        self.stackIndex.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()