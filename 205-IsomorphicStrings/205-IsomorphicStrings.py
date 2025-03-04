class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        see = {}
        tee = {}

        for i in range(len(s)):
            if s[i] not in see and t[i] not in tee:
                see[s[i]] = t[i]
                tee[t[i]] = s[i]
            elif s[i] not in see or t[i] not in tee:
                return False

            elif see[s[i]] != t[i] or tee[t[i]] != s[i]:
                return False

        return True