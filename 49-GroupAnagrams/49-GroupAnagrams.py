class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c)-ord("a")] += 1
            
            tmp = ",".join([str(x) for x in arr])
            if not tmp in seen:
                seen[tmp] = [s]
            else:
                seen[tmp].append(s)

        for k,v in seen.items():
            res.append([x for x in v])

        return res