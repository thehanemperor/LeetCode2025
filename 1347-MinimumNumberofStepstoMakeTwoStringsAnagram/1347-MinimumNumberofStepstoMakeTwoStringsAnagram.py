class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0]*26
        second = [0] *26
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            count[ord(char1)-ord("a")] += 1
            count[ord(char2)-ord("a")] -= 1

        res = 0
        for i in range(26):
            res += max(0, count[i])

        return res