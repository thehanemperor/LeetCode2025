class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False

        see = {}
        tee = {}

        for i in range(len(pattern)):
            if pattern[i] not in see and arr[i] not in tee:
                see[pattern[i]] = arr[i]
                tee[arr[i]] = pattern[i]

            elif pattern[i] not in see or arr[i] not in tee:
                return False
            
            elif see[pattern[i]] != arr[i] or tee[arr[i]] != pattern[i]:
                return False

        return True

       

            
 