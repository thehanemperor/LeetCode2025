class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count1 = Counter(s1)
        count2 = Counter(s2)

        if count1 != count2:
            return False
        
        swap = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap += 1

        return swap==2