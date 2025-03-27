# Last updated: 3/27/2025, 12:16:30 AM
class Trie:
    def __init__(self):
        self.node = {}
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        res = []
        for word in words:
            root = trie.node
            
            for i in range(len(word)):
                if word[i] in root:
                    root = root[word[i]].node
                else:
                    if i == len(word)-1:
                        root[word[i]] = Trie()
                        res.append(word)
                    else:
                        break

        longest = 0
        if not res:
            return ""
        for w in res:
            longest = max(longest,len(w))
        print(res)

        ret = []
        for w in res:
            if len(w) == longest:
                ret.append(w)
        ret.sort()
        return ret[0]        
        