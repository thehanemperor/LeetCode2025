class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.suggestion = []
            
            def add_sugestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        products.sort()
        
        root = TrieNode()
        for p in products:
            
            node = root
            for char in p:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.add_sugestion(p)
        
        result, node = [], root
        for char in searchWord:
            
            if char not in node.children:
                result.append([])
                node = TrieNode()
            else:
                node = node.children[char]
                result.append(node.suggestion)
        return result