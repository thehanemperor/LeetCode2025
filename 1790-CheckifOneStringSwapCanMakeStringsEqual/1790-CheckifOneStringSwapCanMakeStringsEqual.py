class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        seen1 = Counter(s1)
        seen2 = Counter(s2)
        if seen1 != seen2:
            return False

        wrong = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                wrong += 1

        return wrong <=2