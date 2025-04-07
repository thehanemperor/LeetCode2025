# Last updated: 4/7/2025, 1:19:38 AM
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        sub_strings = collections.defaultdict(set)
        for idx, s in enumerate(arr):
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    sub_strings[s[i : j]].add(idx)
        
        res = []
        for idx, s in enumerate(arr):
            n = len(s)
            match = []
            for i in range(n):
                for j in range(i + 1, n + 1):
                    if len(sub_strings[s[i : j]]) == 1: match.append(s[i : j])
            match.sort(key=lambda x : (len(x), x))
            if not match: res.append("")
            else: res.append(match[0])
        return res