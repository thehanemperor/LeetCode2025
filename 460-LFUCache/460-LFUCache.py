class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq2key = {}
        self.key2freq = {}
        self.cache = {}
        self.minFreq = 0

    def get(self, key: int) -> int:
        print("get",key)
        if key not in self.cache:
            return -1
        val = self.cache[key]
        oldFreq = self.key2freq[key]
        self.key2freq[key]+=1
        # print(self.freq2key)
        self.freq2key[oldFreq].pop(key)
        if not self.freq2key[oldFreq]:
            self.freq2key.pop(oldFreq)
        if oldFreq+1 not in self.freq2key:
            self.freq2key[oldFreq+1] = OrderedDict([(key,1)])
        else:
            self.freq2key[oldFreq+1][key] = 1
        if self.minFreq not in self.freq2key:
            self.minFreq+=1
        
        return val
        

    def put(self, key: int, value: int) -> None:
        # print("put",key,value)
        if self.capacity == 0:
            return 
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return 
        
        if len(self.cache) == self.capacity:
            delkey,val = self.freq2key[self.minFreq].popitem(last=False)
            self.cache.pop(delkey)
            self.key2freq.pop(delkey)
        self.cache[key] = value
        self.key2freq[key] = 1
        if 1 in self.freq2key:
            self.freq2key[1][key] = 1
        else:
            self.freq2key[1] = OrderedDict([(key,1)])
        self.minFreq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)