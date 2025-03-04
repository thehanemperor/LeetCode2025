class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        see = Counter(s)
        tee = Counter(t)
        return see == tee