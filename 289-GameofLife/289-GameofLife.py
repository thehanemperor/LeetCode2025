class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = Counter(magazine)
        for c in ransomNote:
            if c not in seen or seen[c] == 0:
                return False
            seen[c] -= 1

        return True