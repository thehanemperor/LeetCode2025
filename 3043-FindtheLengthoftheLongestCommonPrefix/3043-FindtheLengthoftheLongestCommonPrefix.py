class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        dig1 = [str(num) for num in arr1]
        dig2 = [str(num) for num in arr2]
        trie = {}
        for num in dig1:
            check = trie
            for char in num:
                if char not in check:
                    check[char] = {}
                check = check[char]

        res = 0
        for num in dig2:
            check = trie
            curr = 0
            for char in num:
                if char in check:
                    curr += 1
                    check = check[char]
                else:
                    break
            
            res = max(res,curr)

        return res