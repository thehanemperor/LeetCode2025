class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n -1
        count = 0
        while i>=0:
            if s[i] != " ":
                break
            
            i -= 1

        while i >=0:
            if s[i] == " ":
                break
            count += 1
            i -= 1
        return count