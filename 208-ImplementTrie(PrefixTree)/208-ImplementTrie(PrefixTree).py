class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False
    
    def containsKey(self,char):
        return self.links[ord(char) - ord("a")] != None
    
    def get(self,char):
        return self.links[ord(char)-ord("a")]

    def put(self,char):
        self.links[ord(char)-ord("a")] = TrieNode()

    def setEnd(self):
        self.isEnd = True
    
    def isEnd(self):
        return self.isEnd
class Trie:

    def __init__(self):
        self.tree = TrieNode()

    def insert(self, word: str) -> None:
        root = self.tree
        for char in word:
            if root.containsKey(char):
                root = root.get(char)
            else:
                root.put(char)
                root = root.get(char)
        root.setEnd()

    def search(self, word: str) -> bool:
        root = self.tree
        for char in word:
            if not root.get(char):
                return False
            root = root.get(char)
        if not root.isEnd:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self.tree
        for char in prefix:
            if not root.get(char):
                return False
            root = root.get(char)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)