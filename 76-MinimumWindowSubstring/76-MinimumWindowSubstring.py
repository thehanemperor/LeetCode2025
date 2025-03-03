class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = Counter(t)
        left = right = 0
        seen = {}
        formed = 0
        res = [float("inf"),-1,-1]
        while right < len(s):
            curr = s[right]
            seen[curr] = seen.get(curr,0) + 1
            if curr in check and seen[curr]==check[curr]:
                formed += 1
            
            while left <=right and formed == len(check):
                if right - left + 1 < res[0]:
                    res = [right-left+1,left,right]
                seen[s[left]] -= 1
                if s[left] in check and seen[s[left]] < check[s[left]]:
                    formed -= 1
                
                left += 1

            right += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]