class TrieNode:
    def __init__(self):
        self.node = {}
        self.startHere = 0
        self.endHere = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.node:
                root.node[char] = TrieNode()
            root = root.node[char]
            root.startHere += 1
        root.endHere += 1

    def countWordsEqualTo(self, word: str) -> int:
        root = self.root
        for char in word:
            if char not in root.node:
                return 0
            root = root.node[char]

        return root.endHere

    def countWordsStartingWith(self, prefix: str) -> int:
        root = self.root
        for char in prefix:
            if char not in root.node:
                return 0
            root = root.node[char]
        return root.startHere

    def erase(self, word: str) -> None:
        root = self.root
        for char in word:
            root = root.node[char]
            root.startHere -= 1
        root.endHere -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)